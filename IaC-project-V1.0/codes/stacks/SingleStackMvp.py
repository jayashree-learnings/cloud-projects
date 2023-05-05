
from aws_cdk import (Stack, aws_ec2 as ec2, aws_s3 as s3,
                     aws_s3_deployment as s3deploy, 
                     aws_iam as iam, aws_kms as kms, 
                     aws_backup as backup, aws_events as events, 
                     Tags, Duration)
from constructs import Construct
import aws_cdk as cdk
from aws_cdk.aws_s3_assets import Asset


class SingleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #proj_name = self.node.try_get_context("project_name")
        #env_name = self.node.try_get_context("env")

        admin_ip = "87.210.71.143/32"

        # define the vpc to launch web server 
        webServer_vpc = ec2.Vpc(
                    self, "WebServerVpcA",
                    availability_zones=["eu-central-1a", "eu-central-1b"],
                    ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
                    nat_gateways=0,
                    subnet_configuration=[ec2.SubnetConfiguration(name="public", cidr_mask=25, subnet_type=ec2.SubnetType.PUBLIC)]
                    )
            
        # define the vpc to launch admin server 
        adminServer_vpc = ec2.Vpc(
                     self, "AdminServerVpcB",
                     availability_zones=["eu-central-1a", "eu-central-1b"],
                     ip_addresses= ec2.IpAddresses.cidr("10.20.20.0/24"),
                     nat_gateways = 0,
                     subnet_configuration = [ec2.SubnetConfiguration(name = "public" , cidr_mask = 25, subnet_type = ec2.SubnetType.PUBLIC)]
                     )

        # public subnets of webServerVpc (Vpc A)
        publicSubnets_webServerVpc = webServer_vpc.public_subnets
        
        # list of cidr block of public subnets in vpc A
        cidrRange_publicSubnetsOfWebServerVpc = [
            pubSubnet.ipv4_cidr_block for pubSubnet in publicSubnets_webServerVpc]
        
        # The first element of the list corresponds to the cidr of public subnet in which web server is launched
        cidrBlock_webServer = cidrRange_publicSubnetsOfWebServerVpc[0]

        print("web server launched in ", cidrBlock_webServer)
        
        # public subnets of adminServerVpc (Vpc B)
        publicSubnets_adminServerVpc = adminServer_vpc.public_subnets

        # list of cidr block of public subnets in vpc B
        cidrRange_publicSubnetsOfAdminServerVpc = [pubSubnet.ipv4_cidr_block for pubSubnet in publicSubnets_adminServerVpc]

        # The second  element of the list corresponds to the cidr of public subnet in which web server is launched
        cidrBlock_adminServer = cidrRange_publicSubnetsOfAdminServerVpc[1]

        print ("admin server launched in ", cidrBlock_adminServer)
        
        # NACL of Web Server

        webServer_nacl = ec2.NetworkAcl(
                       self, "WebSeverNetworkAcl",
                       vpc = webServer_vpc,    
                       network_acl_name = "WebServerNACL",
                       subnet_selection = ec2.SubnetSelection(availability_zones=["eu-central-1a", "eu-central-1b"],
                                                     one_per_az=False,
                                                     subnet_type=ec2.SubnetType.PUBLIC
                                                     )
                      )

        # Web server receives http(s) requests at ports 80 or 443 from any ipv4 and sends the response as outbound traffic to ephemeral ports
        webServer_nacl.add_entry(
                      'AllowHttpIngressTrafficToWebServer',
                       cidr = ec2.AclCidr.any_ipv4(),
                       direction = ec2.TrafficDirection.INGRESS,
                       rule_number = 100, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name = 'AllowHttpIngressRequests',
                       traffic = ec2.AclTraffic.tcp_port(80)
                       ) 

        webServer_nacl.add_entry(
                      'AllowEphemeralEgressResponseTrafficFromWebServer',
                       cidr = ec2.AclCidr.any_ipv4(),
                       direction = ec2.TrafficDirection.EGRESS,
                       rule_number = 110, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name= 'AllowEphemeralEgress',
                       traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
                       ) 
        

        # Web server receives requests at port 22 from admin server and sends the same ipv4 range 
        # as the outbound traffic to ephemeral ports of admin server

        webServer_nacl.add_entry(
                      'AllowSSHFromAdminServerVpcToThePublicSubnetsOfWebServerVpcA',
                       cidr = ec2.AclCidr.ipv4(adminServer_vpc.vpc_cidr_block),
                       direction = ec2.TrafficDirection.INGRESS,
                       rule_number = 120, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name= 'AllowSSHIngressFromAdminVPC',
                       traffic = ec2.AclTraffic.tcp_port(22)
                       )   



        webServer_nacl.add_entry(
                      'AllowEphemeralTrafficFromWebServerToEphemeralPortOfAdminServer',
                       cidr = ec2.AclCidr.ipv4(adminServer_vpc.vpc_cidr_block),
                       direction = ec2.TrafficDirection.EGRESS,
                       rule_number = 120, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name= 'AllowEphemeralEgressToAdminServer',
                       traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
                       ) 
               
        # Request for apache downloads originate from web server at ephemeral ports. It sends out the request 
        # as egress traffic to port 80 or 443 and receives the response as ingress traffic on the ephemeral ports 
        
        webServer_nacl.add_entry(
                      'AllowHttpEgressTrafficFromWebServerForDownloads',
                       cidr = ec2.AclCidr.any_ipv4(), 
                       direction = ec2.TrafficDirection.EGRESS,
                       rule_number = 140, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name = 'AllowHttpEgressTrafficFromWebServer',
                       traffic = ec2.AclTraffic.tcp_port(80)
                       ) 


        webServer_nacl.add_entry(
                      'AllowHttpsEgressTrafficFromWebServerForDownloads',
                       cidr = ec2.AclCidr.any_ipv4(), 
                       direction = ec2.TrafficDirection.EGRESS,
                       rule_number = 150, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name = 'AllowHttpsEgressTrafficFromWebServer',
                       traffic = ec2.AclTraffic.tcp_port(443)
                       ) 
        
        webServer_nacl.add_entry(
                      'AllowEphemeralIngressResponseTrafficFromInternet',
                       cidr = ec2.AclCidr.any_ipv4(),
                       direction = ec2.TrafficDirection.INGRESS,
                       rule_number = 150, 
                       rule_action = ec2.Action.ALLOW, 
                       network_acl_entry_name= 'AllowEphemeralIngress',
                       traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
                       ) 
                
        # defining SG for web server
        webServer_sg = ec2.SecurityGroup(
                     self, 
                    "webserverSG", 
                    vpc=webServer_vpc, 
                    allow_all_outbound=True, 
                    description="WebServerSG"
                    )

      # allows ingress http webtraffic

        webServer_sg.add_ingress_rule(
                    ec2.Peer.any_ipv4(),
                    ec2.Port.tcp(80),
                   "allowsHttpTrafficFromEverywhere"
                   )

        # allows ingress https traffic
        webServer_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            "allowsHttpsTrafficFromEverywhere"
            )

   
        # allows SSH ingress traffic from admin server vpc
        webServer_sg.add_ingress_rule(
            ec2.Peer.ipv4('10.20.20.0/24'),  
            ec2.Port.tcp(22),
            "allowsSSHFromAdminServer"
        )

        # NACL of Admin Server

        adminServer_nacl = ec2.NetworkAcl(
                         self, "adminServerNetworkAcl",
                         vpc = adminServer_vpc,    
                         network_acl_name = "adminServerNACL",
                         subnet_selection = ec2.SubnetSelection(
                                         availability_zones=["eu-central-1a", "eu-central-1b"],
                                         one_per_az=False,
                                         subnet_type=ec2.SubnetType.PUBLIC
                                         )
                        )

        # Admin server receives the RDP request at port 3389 from administrator office and send the response 
        # as outbound traffic to one of the ephemeral ports of the office laptop

        adminServer_nacl.add_entry(
                         'AllowRdpIngressTrafficToAdminServerFromAdministratorOffice',
                          cidr = ec2.AclCidr.ipv4(admin_ip), 
                          rule_number = 100, 
                          direction = ec2.TrafficDirection.INGRESS,
                          rule_action = ec2.Action.ALLOW, 
                          network_acl_entry_name = 'AllowRDPIngress',
                          traffic = ec2.AclTraffic.tcp_port(3389)
                          ) 

        adminServer_nacl.add_entry(
                        'AllowRdpEgressTrafficFromAdminServer',
                         cidr = ec2.AclCidr.ipv4(admin_ip), 
                         rule_number = 100, 
                         direction = ec2.TrafficDirection.EGRESS,
                         rule_action = ec2.Action.ALLOW, 
                         network_acl_entry_name = 'AllowAllEgressFromAdminServerToOfficeLaptop',
                         traffic = ec2.AclTraffic.tcp_port_range(1024, 65535)
                         ) 
       
        # Admin server sends SSH request to  port 22 of web server as outbound traffic and receives the response at one of 
        # ephemeral ports of office laptop

        adminServer_nacl.add_entry(
                        'AllowSshEgressTrafficFromAdminServer',
                         cidr = ec2.AclCidr.ipv4(webServer_vpc.vpc_cidr_block), 
                         rule_number = 110, 
                         direction = ec2.TrafficDirection.EGRESS,
                         rule_action = ec2.Action.ALLOW, 
                         network_acl_entry_name = 'AllowAllSSHEgressFromAdminServer',
                         traffic = ec2.AclTraffic.tcp_port(22)
                         ) 

        adminServer_nacl.add_entry(
                        'AllowSSHIngressTrafficFromWebServerAsResponse',
                         cidr = ec2.AclCidr.ipv4(webServer_vpc.vpc_cidr_block),
                         rule_number = 110, 
                         direction = ec2.TrafficDirection.INGRESS,
                         rule_action = ec2.Action.ALLOW, 
                         network_acl_entry_name = 'AllowIngressToAdminServerFromCidrOfWebServerVpcA',
                         traffic = ec2.AclTraffic.tcp_port_range(1024, 65535))
 

       # defining SG for admin server
        adminServer_sg = ec2.SecurityGroup(
                         self, 
                         "adminServerSG", 
                         vpc = adminServer_vpc,
                         allow_all_outbound=True, 
                         description="AdminServerSG"
                         )

        adminServer_sg.add_ingress_rule(
                        ec2.Peer.ipv4(admin_ip),
                        ec2.Port.tcp(3389),
                        "allowsRdpTrafficFromAdministratorHomeOrOfficeOnly"
                         )

        # allows ssh connection from admin office
        adminServer_sg.add_ingress_rule(
                      ec2.Peer.ipv4(admin_ip),
                      ec2.Port.tcp(22),
                      "allowsSSHTrafficFromAdministratorHomeOrOfficeOnly"
                       )
        

        # defining web server

        amzn_linux_img = ec2.AmazonLinuxImage(
                        generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                        edition=ec2.AmazonLinuxEdition.STANDARD,
                        virtualization=ec2.AmazonLinuxVirt.HVM,
                        storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                        )

        webServer_keyPair = ec2.CfnKeyPair(
                          self, 
                          "WebServerKeyPair", 
                          key_name="webServerKeyPair1234", 
                          tags = [cdk.CfnTag(key = "Name" , value =  "WebServerKeyPair")] 
                          )
        
        webServer_EBSVol_KMSKey = kms.Key(
                               self,
                               "webServerEBSVolKey", 
                               alias = "webServerEBSEncryptionKey",
                               removal_policy  = cdk.RemovalPolicy.DESTROY, 
                               enable_key_rotation= True
                               )
                                                          

        webServer_instance = ec2.Instance(
                          self, "WebServer",
                          instance_type = ec2.InstanceType("t2.micro") ,                                         
                          machine_image=amzn_linux_img,
                          vpc=webServer_vpc,
                          vpc_subnets=ec2.SubnetSelection(availability_zones=["eu-central-1a"], subnet_type=ec2.SubnetType.PUBLIC),
                          security_group=webServer_sg,
                          key_name = webServer_keyPair.key_name,
                          block_devices = [ec2.BlockDevice(device_name = '/dev/xvda',
                                       volume = ec2.BlockDeviceVolume.ebs(
                                       volume_size = 8,                                                                                                           
                                       delete_on_termination= True,
                                       encrypted = True,
                                       kms_key = webServer_EBSVol_KMSKey
                                       )
                                     )
                                        ]
                          )

       
        # The user data script is uploaded to the s3 boot strap bucket
        asset = Asset(self, "LocalFileToAsset", path = "./UserData/bootStrapScript.sh")

        # The script is downloaded to the /tmp folder of the web server from the bootstrap s3 bucket
        filePath_webServer = webServer_instance.user_data.add_s3_download_command(
                                    bucket = asset.bucket,
                                    bucket_key = asset.s3_object_key
                                    )

        # The file is executed by the instance
        webServer_instance.user_data.add_execute_file_command(file_path = filePath_webServer)

        asset.grant_read(webServer_instance.role)
                      
        print ("localFile Path returned by s3-download command " , filePath_webServer)

        # image of windows server defined 
        windows_img = ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE)

        # key pair for login is defined
        adminServer_keyPair = ec2.CfnKeyPair(
                            self, 
                            "AdminServerKeyPair", 
                            key_name="adminServerKeyPair1234",
                            tags = [cdk.CfnTag(key = "Name" , value =  "AdminServerKeyPair")] 
                            )
        
        # KMS key for encrypting EBS device
        
        adminServer_EBSVol_KMSKey = kms.Key(
                                  self, 
                                  "adminServerEBSVolKey", 
                                  alias = "adminServerEBSEncryptionKey",
                                  removal_policy  = cdk.RemovalPolicy.DESTROY, 
                                  enable_key_rotation= True
                                  )

        print ("admin server key pair is ", adminServer_keyPair.key_name)
        adminServer_instance = ec2.Instance (
                              self, "AdminServer",
                              instance_type = ec2.InstanceType("t2.micro"),
                              machine_image = windows_img,
                              vpc = adminServer_vpc,
                              vpc_subnets =  ec2.SubnetSelection(availability_zones = ["eu-central-1b"], subnet_type = ec2.SubnetType.PUBLIC ) ,
                              security_group = adminServer_sg,
                              key_name = adminServer_keyPair.key_name,
                              block_devices = [ec2.BlockDevice(
                                             device_name = '/dev/sda1' ,
                                             volume = ec2.BlockDeviceVolume.ebs(
                                                      volume_size = 30,                                                                                                           
                                                      delete_on_termination= True,
                                                      encrypted = True,
                                                       kms_key = adminServer_EBSVol_KMSKey
                                                       )
                                             )
                                            ]

                            )

        # peering connection

        vpcPeering_connection = ec2.CfnVPCPeeringConnection(
                              self, 
                              "VpcAtoVpcB", 
                              vpc_id = adminServer_vpc.vpc_id, 
                              peer_vpc_id= webServer_vpc.vpc_id
                              )

        print ("id of peering concn ", vpcPeering_connection.ref)
        print("The RT to be edited for in vpcA  ", publicSubnets_webServerVpc[0].route_table.route_table_id)
        print("The RT to be edited for in vpcB  ", publicSubnets_adminServerVpc[1].route_table.route_table_id)
        
        # The peering connection id is entered in the route table associated with the public subnet(where the webServer is launched) of Vpc A
        # The traffic destined to the public subnet of the admin server is routed the peering connection.
        ec2.CfnRoute ( 
                self,
                "RouteFromPublicSubnetOfWebServerVpcAToPublicSubnetOfAdminServerVpcB",
                destination_cidr_block = cidrBlock_adminServer,
                route_table_id = publicSubnets_webServerVpc[0].route_table.route_table_id,
                vpc_peering_connection_id = vpcPeering_connection.ref
                )
                     
        # The peering connection id is entered in the route table associated with the public subnet(where the adminServer is launched) of VpcB
        # The traffic destined to the public subnet of the web server is routed the peering connection.
        ec2.CfnRoute ( 
                self,
                "RouteFromPublicSubnetOfAdminServerVpcBToPublicSubnetOfWebServerVpcA",
                destination_cidr_block = cidrBlock_webServer,
                route_table_id = publicSubnets_adminServerVpc[1].route_table.route_table_id,
                vpc_peering_connection_id = vpcPeering_connection.ref
                )

        

        # back up policy of both servers

        server_backUpVault_KMSKey = kms.Key(
                                 self, 
                                 "ServerVaultKey", 
                                 alias = "ServerBackUpVaultEncryptionKey",
                                 removal_policy  = cdk.RemovalPolicy.DESTROY, 
                                 enable_key_rotation= True
                                 )
        
        server_backUpVault = backup.BackupVault(
                            self, 
                            "ServerBackUpVault" , 
                            backup_vault_name = "BackUpVaultServer",
                            encryption_key = server_backUpVault_KMSKey,
                            removal_policy = cdk.RemovalPolicy.DESTROY
                            )

        server_backUpPlan = backup.BackupPlan(self, "BackUpPlanServer", backup_plan_name = "serverBackUpPlan")
        server_backUpPlan.add_selection("Servers-Selection", 
                                            resources = [backup.BackupResource.from_ec2_instance(webServer_instance),
                                                          backup.BackupResource.from_ec2_instance(adminServer_instance)])
                                                                                                  
                                                    
        # Server backUp plan
        server_backUpPlan.add_rule(
              backup.BackupPlanRule(
                       backup_vault= server_backUpVault,
                       rule_name= "BackUpRuleServer"  ,
                       delete_after = Duration.days(7),
                       schedule_expression = events.Schedule.cron(
                                        week_day = '*',
                                        hour = '5',
                                        minute = '0'
                                        )
                     )
            )

                                                                                         
                                                 
                                                 
                                           
        
        
        
                               


