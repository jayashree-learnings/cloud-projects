from certs.certCreateImport import cert_arn
from constructs import Construct
import aws_cdk as cdk
import json
from aws_cdk import (Stack, 
                     aws_ec2 as ec2,
                     aws_kms as kms, 
                     aws_iam as iam,
                     Tags,
                     Duration )
  
class AdminServerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,  adminServer_ebsVolKey:kms.Key, **kwargs) -> None:
        super().__init__(scope,construct_id, **kwargs)
        
        print("this is adminServer stack")

        admin_ip = "87.210.71.143/32"
        adminServer_vpc_cidr = "10.20.20.0/24"
        webServer_vpc_cidr = "10.10.10.0/24"
                    
        # defining the vpc to launch admin server.          
        admin_server_vpc = ec2.Vpc(
            self, "AdminServerVpcB",
            availability_zones=["eu-central-1a", "eu-central-1b"],
            ip_addresses= ec2.IpAddresses.cidr("10.20.20.0/24"),
            nat_gateways = 0,
            subnet_configuration = [ec2.SubnetConfiguration(name = "public" , cidr_mask = 25, subnet_type = ec2.SubnetType.PUBLIC)]
        )
        
        # making it an attribute of this class so as to use it in web server stack
        self.adminServer_vpc = admin_server_vpc

        # NACL of Admin Server
        adminServer_nacl = ec2.NetworkAcl(
            self, "adminServerNetworkAcl",
            vpc = self.adminServer_vpc,  
            network_acl_name = "adminServerNACL",
            subnet_selection = ec2.SubnetSelection(
                availability_zones=["eu-central-1a", "eu-central-1b"],
                one_per_az=False,
                subnet_type=ec2.SubnetType.PUBLIC)
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

        # Admin server  receives  SSH request at  port 22 from administrator laptop and receive response 
        # as outbound traffic to one of the ephemeral ports of the office laptop

        adminServer_nacl.add_entry(
            'AllowSSHIngressTrafficToAdminServerFromAdministratorOffice',
            cidr = ec2.AclCidr.ipv4(admin_ip), 
            rule_number = 120, 
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowRDPIngress',
            traffic = ec2.AclTraffic.tcp_port(22)
        ) 

        adminServer_nacl.add_entry(
            'AllowSSHEgressTrafficFromAdminServer',
            cidr = ec2.AclCidr.ipv4(admin_ip), 
            rule_number = 120, 
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowAllEgressFromAdminServerToOfficeLaptop',
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535)
        ) 

        # Admin server sends SSH request to  port 22 of web server as outbound traffic and receives the response 
        # at one of the ephemeral ports 

        adminServer_nacl.add_entry(
            'AllowingEgressSSHRequestToWebServer',
            cidr = ec2.AclCidr.ipv4(webServer_vpc_cidr), 
            rule_number = 110, 
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowAllSSHRequestAsEgressTrafficFromAdminServer',
            traffic = ec2.AclTraffic.tcp_port(22)
        ) 

        adminServer_nacl.add_entry(
            'AllowSSHIngressTrafficFromWebServerAsResponse',
            cidr = ec2.AclCidr.ipv4(webServer_vpc_cidr),
            rule_number = 110, 
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowIngressToAdminServerFromCidrOfWebServerVpcA',
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535)
        )

        # allowing the internet connections to download openssh at ports 443 and 80

        adminServer_nacl.add_entry(
            'AllowResponseFromOutside',
            cidr = ec2.AclCidr.any_ipv4(),
            rule_number = 130, 
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowIngressToAdminServerFromOutside',
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535)
        )
        
        adminServer_nacl.add_entry(
              'AllowHttpsRequest',
              cidr = ec2.AclCidr.any_ipv4(), 
              rule_number = 130, 
              direction = ec2.TrafficDirection.EGRESS,
              rule_action = ec2.Action.ALLOW, 
              network_acl_entry_name = 'AllowAllHttpsRequestAsEgressTrafficFromAdminServer',
              traffic = ec2.AclTraffic.tcp_port(443)
        ) 
        adminServer_nacl.add_entry(
            'AllowHttpRequest',
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 140, 
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW, 
            network_acl_entry_name = 'AllowAllHttpRequestAsEgressTrafficFromAdminServer',
            traffic = ec2.AclTraffic.tcp_port(80)
        ) 
              
        
      # defining SG for admin server
        adminServer_sg = ec2.SecurityGroup(
            self, 
            "adminServerSG", 
            vpc = self.adminServer_vpc,
            allow_all_outbound=True, 
            description="AdminServerSG"
        )

        adminServer_sg.add_ingress_rule(
              ec2.Peer.ipv4(admin_ip),
              ec2.Port.tcp(3389),
              "allowsRDPTrafficFromAdministratorHomeOrOfficeOnly"
        )
        
        # allows ssh connection from admin office
        adminServer_sg.add_ingress_rule(
              ec2.Peer.ipv4(admin_ip),
              ec2.Port.tcp(22),
              "allowsSSHTrafficFromAdministratorHomeOrOfficeOnly"
        )
        
        # image of windows server defined 
        windows_img = ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE)

        # key pair for login is defined
        adminServer_keyPair = ec2.CfnKeyPair(
            self, 
            "ServersKeyPair", 
            key_name="ServerKeyPair1234",
        )
        Tags.of(adminServer_keyPair).add(key= "name" , value="ServerKeyPair" ) 
        
        # making it an attribute of this class so as to use it another stack
        self.server_keyPair = adminServer_keyPair

       # print("in admin server stack key pair name ", adminServer_keyPair.key_name)


        adminServer_instance = ec2.Instance (
            self, "AdminServer",
            instance_type = ec2.InstanceType("t2.micro"),
            machine_image = windows_img,
            vpc = self.adminServer_vpc,
            vpc_subnets =  ec2.SubnetSelection(availability_zones = ["eu-central-1b"], subnet_type = ec2.SubnetType.PUBLIC ) ,
            security_group = adminServer_sg,
            key_name = adminServer_keyPair.key_name,
            block_devices = [ec2.BlockDevice(
                device_name = '/dev/sda1' ,
                volume = ec2.BlockDeviceVolume.ebs(
                volume_size = 30,                                                                                                           
                delete_on_termination= True,
                encrypted = True,
                kms_key = adminServer_ebsVolKey))]
        )
        
        # installing the ssh sever on windows-admin-server so as to do the "jump connection" from 
        # admin's laptop to the web server directly
        
        user_data = ec2.UserData.for_windows()
        adminServer_instance.user_data.add_commands(
            "<powershell>",
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'"
        )
                 
              
        


        

        







         

                         
                                                 
                                           
        
        
        
                               


                                                                 
                                                 
                                                 
                                           
        
        
        
                               


