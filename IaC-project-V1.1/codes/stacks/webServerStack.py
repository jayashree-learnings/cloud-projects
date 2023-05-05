from certs.certCreateImport import cert_arn
from constructs import Construct
import aws_cdk as cdk
import json
from aws_cdk import (Stack, 
                     aws_ec2 as ec2,
                     aws_s3 as s3,
                     aws_s3_deployment as s3deploy, 
                     aws_iam as iam, aws_kms as kms, 
                     aws_autoscaling as autoscaling,
                     aws_iam as iam,
                     aws_elasticloadbalancingv2 as elbv2,
                     aws_certificatemanager as acm,
                     Tags,
                     Duration )
                     
from aws_cdk.aws_s3_assets import Asset
from aws_cdk .aws_elasticloadbalancingv2 import ApplicationLoadBalancer as alb



class WebServerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, 
                webServer_ebsVolKey:kms.Key, 
                admin_server_vpc = ec2.Vpc, 
                s3_userData_bkt = s3.Bucket,
                webServer_key = ec2.CfnKeyPair, 
                **kwargs) -> None:
        super().__init__(scope,construct_id, **kwargs)
        
        adminServer_vpc_cidr = "10.20.20.0/24"
        webServer_vpc_cidr = "10.10.10.0/24"        
        admin_ip = "87.210.71.143/32"
        adminServer_vpc = admin_server_vpc
        print ("this is web server stack")
        print ("this cert arn imported is ",cert_arn)

        # define the vpc where web server is launched. The cidr is split into 4 equal parts
        webServer_vpc = ec2.Vpc(
            self, 
            "WebServerVpcA",
            availability_zones=["eu-central-1a", "eu-central-1b"],
            ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
            subnet_configuration = [
            ec2.SubnetConfiguration(
                name="public", 
                cidr_mask=26, 
                subnet_type=ec2.SubnetType.PUBLIC),
            ec2.SubnetConfiguration(
                name = "private", 
                cidr_mask = 26, 
                subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS)
                ]
        )

        # defining the amazon linux image for launch template of asg

        amzn_linux_img = ec2.AmazonLinuxImage(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )
             
        # NACL of public subnets in the web server vpc

        webServerVpc_publicSubnet_nacl = ec2.NetworkAcl(
            self, "PublicSubnetNACLofWebServerVpc",
            vpc = webServer_vpc,    
            network_acl_name = "NACLForPublicSubnetOfWebServerVpc",
            subnet_selection = ec2.SubnetSelection(
            availability_zones=["eu-central-1a", "eu-central-1b"],
            one_per_az=False,
            subnet_type=ec2.SubnetType.PUBLIC
                )
        )
               
        webServerVpc_publicSubnet_nacl.add_entry(
            'AllowHttpsRequestAsIngressTrafficToALB',
            cidr  = cdk.aws_ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.INGRESS,
            rule_number =110, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowHttpsIngressRequests',
            traffic = ec2.AclTraffic.tcp_port(443)
        )        
       
        webServerVpc_publicSubnet_nacl.add_entry(
            'AllowHttpRequestAsIngressTrafficToALB',
            cidr  = cdk.aws_ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.INGRESS,
            rule_number = 120, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowHttpIngressRequests',
            traffic = ec2.AclTraffic.tcp_port(80)
        ) 

        webServerVpc_publicSubnet_nacl.add_entry(
            'AllowsEphemeralIngress',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.INGRESS,
            rule_number = 130, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowEphemeralIncomingTraffic',
            traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
        )


        webServerVpc_publicSubnet_nacl.add_entry(
            'AllowsEphemeralEgressTraffic',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.EGRESS,
            rule_number = 110, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowEphemeralEgress',
            traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
        )
        
        webServerVpc_publicSubnet_nacl.add_entry(
            'AllowHttpEgressForPort80',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.EGRESS,
            rule_number = 120, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowHttpEgressOut',
            traffic = ec2.AclTraffic.tcp_port(80)
        )
                        
        webServerVpc_publicSubnet_nacl.add_entry(
            'AllowEgressForPort443',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.EGRESS,
            rule_number = 310, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowHttpsEgress',
            traffic = ec2.AclTraffic.tcp_port(443)
        )
        
        #  NACL of private subnets
        webServerVpc_privateSubnet_nacl = ec2.NetworkAcl(
            self, "PrivateSubnetNACLofWebSeverVpc",
            vpc = webServer_vpc,    
            network_acl_name = "NACLForPrivateSubnetOfWebServerVpc",
            subnet_selection = ec2.SubnetSelection(
                availability_zones=["eu-central-1a", "eu-central-1b"],
                one_per_az=False,
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
        )

        webServerVpc_privateSubnet_nacl.add_entry(
            'AllowSSHFromAdminServerVpcToThePrivateSubnetsOfWebServerVpcA',
            cidr = ec2.AclCidr.ipv4(adminServer_vpc.vpc_cidr_block),
            direction = ec2.TrafficDirection.INGRESS,
            rule_number = 110, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowSSHIngressFromAdminVPC',
            traffic = ec2.AclTraffic.tcp_port(22)
        ) 
 
        webServerVpc_privateSubnet_nacl.add_entry(
            'AllowsIngressForALB',
            cidr = ec2.AclCidr.ipv4("10.10.10.0/24"),
            direction = ec2.TrafficDirection.INGRESS,
            rule_number = 200, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowALBIngress',
            traffic = ec2.AclTraffic.tcp_port(80)
        )
          
        webServerVpc_privateSubnet_nacl.add_entry(
            'AllowsEphemeralIngressFromAnywhere',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.INGRESS,
            rule_number = 120, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowEphemeralIngress',
            traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
        )
        
        webServerVpc_privateSubnet_nacl.add_entry(
            'AllowEgressToAnywhere',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.EGRESS,
            rule_number = 120, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowEphemeralEgressToAnywhere',
            traffic = ec2.AclTraffic.tcp_port_range(1024,65535)
        ) 

        webServerVpc_privateSubnet_nacl.add_entry(
            'AllowingEgressAtPort80',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.EGRESS,
            rule_number = 130, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowingHttpEgressForPorts80',
            traffic = ec2.AclTraffic.tcp_port(80)
        )
         
        webServerVpc_privateSubnet_nacl.add_entry(
            'AllowingEgressAtPort443',
            cidr = ec2.AclCidr.any_ipv4(),
            direction = ec2.TrafficDirection.EGRESS,
            rule_number = 140, 
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name= 'AllowingEgressForPort443',
            traffic = ec2.AclTraffic.tcp_port(443)
        )

        # defining the SG for web server
        webServerLaunchTemplate_sg = ec2.SecurityGroup(
            self, 
            "webServerLaunchTemplateSG", 
            vpc = webServer_vpc, 
            allow_all_outbound=True, 
            description="WebServerLaunchTemplateSG"
        )

        webServerLaunchTemplate_sg.add_ingress_rule(
                ec2.Peer.ipv4(webServer_vpc_cidr),
                ec2.Port.tcp(80),
                "allowsHttpTrafficFromVpcOfWebServerForwardedByALB" 
        )

        webServerLaunchTemplate_sg.add_ingress_rule(
            ec2.Peer.ipv4(adminServer_vpc_cidr),  
            #ec2.Peer.ipv4('0.0.0.0/0'),
            ec2.Port.tcp(22),
            "allowsSSHFromAdminServer"
        )
        
        webServer_LaunchTemplate = ec2.LaunchTemplate(
                  self,
                  "WebSeverLaunchTemplateForASG", 
                   launch_template_name = "LaunchTemplateWebServer",
                   machine_image = amzn_linux_img,
                   instance_type = ec2.InstanceType("t2.micro"),
                   block_devices = [
                       ec2.BlockDevice(
                            device_name = '/dev/xvda',
                            volume = ec2.BlockDeviceVolume.ebs(
                                volume_size = 8,                                                                                                           
                                delete_on_termination= True,
                                encrypted = True,
                                kms_key = webServer_ebsVolKey
                            )
                        )
                   ],
                                        
                  key_name = webServer_key.key_name,    # using the value imported from admin stack
                  security_group = webServerLaunchTemplate_sg,
                  user_data = ec2.UserData.for_linux() ,
                  role = iam.Role(
                      self, 
                      "RoleForS3", 
                       assumed_by =  iam.ServicePrincipal("ec2.amazonaws.com"),
                       description = "LaunchTemplateRole"
                      )                             
        ) 

        #  The user data script is downloaded from the s3  bucket to the /tmp folder of the linux ec2 instance      
        filePath_webServer = webServer_LaunchTemplate.user_data.add_s3_download_command(
                    bucket = s3_userData_bkt,
                    bucket_key = "bootStrapScript.sh"
        )

        #  The file is executed by the instance
        webServer_LaunchTemplate.user_data.add_execute_file_command(file_path = filePath_webServer)
        s3_userData_bkt.grant_read(webServer_LaunchTemplate.role)
                           
        # Defining the ASG
        webServer_asg = autoscaling.AutoScalingGroup(
                self,
                "WebServerASG",
                vpc = webServer_vpc,
                launch_template = webServer_LaunchTemplate ,
                min_capacity = 1,
                desired_capacity = 2,
                max_capacity = 3,
                vpc_subnets = ec2.SubnetSelection(
                               availability_zones = ["eu-central-1a","eu-central-1b"],
                               subnet_type = ec2.SubnetType.PRIVATE_WITH_EGRESS),
                cooldown = Duration.minutes(15), 
                health_check = autoscaling.HealthCheck.ec2(grace = Duration.minutes(6))            
        )

        # adding tags to asg so as to use it in the back up plan
        Tags.of(webServer_asg).add(key= "name" , value="AutoscalingGroupOfWebServer" ) 
        
        # Application Load Balancer-Security Group        
        webServerALB_sg = ec2.SecurityGroup(
                self, 
                "webServerALBSecurityGroup", 
                 vpc = webServer_vpc, 
                 allow_all_outbound=True, 
                 description="WebServerALBSG"
        )
        webServerALB_sg.add_ingress_rule(
                    ec2.Peer.any_ipv4(),
                    ec2.Port.tcp(80),
                   "allowsHttpTrafficFromEverywhere" 
        )
        webServerALB_sg.add_ingress_rule(
                    ec2.Peer.any_ipv4(),
                    ec2.Port.tcp(443),
                   "allowsHttpsTrafficFromEverywhere" 
        )

        # defining the ALB
        webServer_alb = alb(
               self,
               "WebServerALB",
               load_balancer_name= "WebServerALB" ,
               vpc = webServer_vpc,
               vpc_subnets = ec2.SubnetSelection(
                     availability_zones = ["eu-central-1a","eu-central-1b"],
                     subnet_type = ec2.SubnetType.PUBLIC),
               internet_facing = True ,
               security_group = webServerALB_sg                         
        )
        
        # using the variable imported from the certCreateImport.py file
        certificate_arn = cert_arn               
        alb_cert = acm.Certificate.from_certificate_arn(self, "ImportCertificateFromArn",certificate_arn = certificate_arn)

        # defining the listener and redirecting the traffic                
        alb_listener = webServer_alb.add_listener( 
                "ALBListener",
                 port = 443,
                 open = True,
                 certificates =   [alb_cert],
                 ssl_policy = elbv2.SslPolicy.FORWARD_SECRECY_TLS12          
        )
        webServer_alb.add_redirect(source_port = 80, target_port = 443)

       # adding target group to listener and defining the health checks 
        alb_listener.add_targets(
                "ASGaddedAsTargetGroupToListener",
                 port = 80,
                 targets = [webServer_asg] ,
                 health_check =  elbv2.HealthCheck(
                      enabled = True,
                      port = "80",
                      healthy_threshold_count = 2,
                      unhealthy_threshold_count = 2,
                      path = '/',
                      interval = Duration.seconds(5),
                      timeout = Duration.seconds(2)
                 )  
       )
        
        # public subnets of webServerVpc (Vpc A)
        publicSubnets_webServerVpc = webServer_vpc.public_subnets
        privateSubnets_webServerVpc = webServer_vpc.private_subnets

        # public subnets of adminServerVpc (Vpc B)
        publicSubnets_adminServerVpc = adminServer_vpc.public_subnets
        
        # list of cidr block of public subnets in vpc A
        cidrRange_publicSubnetsOfWebServerVpc = [
            pubSubnet.ipv4_cidr_block for pubSubnet in publicSubnets_webServerVpc]
        print("public subnet cidr range list is ", cidrRange_publicSubnetsOfWebServerVpc)
              

        # list of cidr block of private subnets in vpc A
        cidrRange_privateSubnetsOfWebServerVpc = [
            privateSubnet.ipv4_cidr_block for privateSubnet in privateSubnets_webServerVpc]
        print("web server launched in private subnets  ", cidrRange_privateSubnetsOfWebServerVpc)
                
        # list of cidr block of public subnets in vpc B
        cidrRange_publicSubnetsOfAdminServerVpc = [pubSubnet.ipv4_cidr_block for pubSubnet in publicSubnets_adminServerVpc]

        # The second  element of the list corresponds to the cidr of public subnet in which admin server is launched
        cidrBlock_adminServer = cidrRange_publicSubnetsOfAdminServerVpc[1]
        print ("admin server launched in ", cidrBlock_adminServer)

        
        # defining the peering connection between the 2 vpcs
        vpcPeering_connection = ec2.CfnVPCPeeringConnection(
                self, 
                "VpcAtoVpcB", 
                 vpc_id = adminServer_vpc.vpc_id, 
                 peer_vpc_id= webServer_vpc.vpc_id
        )
        
       # editing the route tables of private subnets of webServer-vpc      
       # The traffic destined to the public subnet of the admin server is routed to the peering connection.
        i = 1
        for private_subnet in privateSubnets_webServerVpc:
            ec2.CfnRoute( 
                self,
                "RouteFromPrivateSubnetOfWebServerVpcAToPublicSubnetOfAdminServerVpcB" + str(i),
                destination_cidr_block = adminServer_vpc_cidr,
                route_table_id =  private_subnet.route_table.route_table_id,
                vpc_peering_connection_id = vpcPeering_connection.ref )              
            i += 1
                         
        # The peering connection id is entered in the route table associated with the public subnet(where the adminServer is launched) of VpcB
        # The traffic destined to the private subnets of the web server is routed the peering connection.
        
        j = 1
        for public_subnet in publicSubnets_adminServerVpc:
            ec2.CfnRoute ( 
                self,
                "RouteFromPublicSubnetOfAdminServerVpcBToPrivateSubnetsOfWebServerVpcA" + str(j),
                destination_cidr_block = "10.10.10.0/24",
                route_table_id = public_subnet.route_table.route_table_id ,
                vpc_peering_connection_id = vpcPeering_connection.ref)
            j += 1
        


        
        













         

                         
                                                 
                                           
        
        
        
                               


                                                                 
                                                 
                                                 
                                           
        
        
        
                               


