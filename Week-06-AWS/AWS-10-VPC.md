# AWS VPC
AWS Virtual Private Cloud (VPC) is a virtual network closely resembling the traditional network in a data centre. Each VPC is logically isolated from other virtual networks in the AWS cloud.

## Key terminologies
public subnet - A subnet which has internet access to it specified by the associated route table.

private subnet - A subnet which is not accessible via internet and the associated route table does not route to internet gate way.

NATgateway - Network Address Translator gateway is used in private subnets so that the instances inside it can communicate to the outside resources, but outside resources cannot access those instances.

internet gateway - The connecting device which allows the communication between internet and the resources.

route table - The table with entries called routes which direct the network traffic 

## Exercise
1. Exercise 1
Allocate an Elastic IP address to your account. Use the Launch VPC Wizard option to create a new VPC with the following requirements:

    - Region: Frankfurt (eu-central-1)

    - VPC with a public and a private subnet

    - Name: Lab VPC

    - CIDR: 10.0.0.0/16

    ● Requirements for the public subnet:

    - Name: Public subnet 1

    - CIDR: 10.0.0.0/24

    - AZ: eu-central-1a

    ● Requirements for the private subnet:

    - Name: Private subnet 1

    - CIDR: 10.0.1.0/24

    - AZ: eu-central-1a

2. Create an additional public subnet without using the wizard with the following requirements:
    - VPC: Lab VPC
    - Name: Public Subnet 2
    - AZ: eu-central-1b
    -CIDR: 10.0.2.0/24

    Create an additional private subnet without using the wizard with the following requirements:
    - VPC: Lab VPC
    - Name: Private Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.3.0/24
    - View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.

    ● Explicitly associate the private route table with your two private subnets.

    ● View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.

    ● Explicitly associate the public route table to your two public subnets.

3. Create a Security Group with the following requirements:
    - Name: Web SG
    - Description: Enable HTTP Access
    - VPC: Lab VPC
    - Inbound rule: allow HTTP access from anywhere
    - Outbound rule: Allow all traffic

4. Launch an EC2 instance with the following requirements:
    - AMI: Amazon Linux 2
    - Type: t3.micro
    - Subnet: Public subnet 2
    - Auto-assign Public IP: Enable
    - User data:
#!/bin/bash
#Install Apache Web Server and PHP
yum install -y httpd mysql php
#Download Lab files
wget
https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1
/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
#Turn on web server
chkconfig httpd on
service httpd start

    - Tag:
    Key: Name
    Value: Web server
    - Security Group: Web SG
    - Key pair: no key pair
-  Connect to your server using the public IPv4 DNS name.
 
### Sources
https://cjrequena.com/2020-06-23/aws-vpc-without-wizard-en

https://docs.amazonaws.cn/en_us/vpc/latest/userguide/vpc-getting-started.html

https://docs.amazonaws.cn/en_us/vpc/latest/userguide/configure-your-vpc.html

https://www.simplilearn.com/tutorials/aws-tutorial/aws-vpc

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html

### Overcome challenges
Had to understand how to direct the traffic in private and public subnets. Understood it while implementing the route table, nat gateway, internet gateway.

### Results
The VPC, private and public subnets in the AZ eu-central-1a were created using the create VPC option. The NAT GW was created in public subnet. Then private and public subnets were created in that VPC in the AZ eu-central-1b. In the public route  table, the route to the IGW was specified and it was attached to the 2 public subnets. In the private route table, for all the traffic going outside (0.0.0.0./0), route was specified to NGW placed in the public subnet. An elastic ip was also associated to the NGW which it uses to connect to the internet. 
An ec2 instance was created in public subnet of AZ-1b. The user data was given to launch httpd. A security group was created and attached to the ec2.    

launching the VPC
##### ![AWS-10-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/01-LAbVPC-launchwizard.PNG)

public and private sub nets
##### ![AWS-10-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/02-publicAndPrivateSubnets.PNG)

Internet Gate Way
##### ![AWS-10-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/03-igwLabVPC.PNG)

NAT GateWay- Elastic ip address
##### ![AWS-10-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/04-NATGW-EIP.PNG)

public subnet in AZ-1b
##### ![AWS-10-05a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/05a-publicsubnet1b.PNG)

private subnet in AZ-1b
##### ![AWS-10-05b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/05b-privatesubnet1b.PNG)

Private RT with NAT
##### ![AWS-10-06a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/06a-privateRTrouteswithNAT.PNG)

Private RT associated to private subnet
##### ![AWS-10-06b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/06b-privaeteRTassociatedtoprivatesubnets.PNG)

Public RT with IGW
##### ![AWS-10-07a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/07a-publicRTrotesWithIGW.PNG)

Public RT associated to public subnet
##### ![AWS-10-07b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/07b-publicRTassociatedtopublicsubnets.PNG)

Security Group for instance
##### ![AWS-10-08](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/08-SGForLabVPC.PNG)

public DNS of the server
##### ![AWS-10-09a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/09a-PubliDNSofServer.PNG)

security group fo the server
##### ![AWS-10-09b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/09b-SGOfwebserver test.PNG)

accessing the server by the public DNS name
##### ![AWS-10-10](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-10/10-accessthesiteusingpublicDNSname.PNG)


