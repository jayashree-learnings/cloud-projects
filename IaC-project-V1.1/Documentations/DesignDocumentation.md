# Design features of V1.1

The design decisions of the architecture is as follows
 
- VPC  
   - 2 vpcs 
    - webServer-vpc with cidr range cidr range of 10.10.10.0/24. 
    - adminServer-vpc with cidr range of 10.20.20.20/24 
    - Each vpc has 2 Azs(eu-central-1a, eu-central-1b)
    - In each Az of the   web server vpc, there is one public subnet and one private subnet.  The 4 subnets are equally divided. 
    - cidr range of public subnets is ['10.10.10.0/26', '10.10.10.64/26'] 
    - private subnets has the cidr range of ['10.10.10.128/26', '10.10.10.192/26']. 
    - each subnet of webServer-vpc can have 64 ip addresses 
    - The ALBs are attached to the public subnets. The ASG launches web servers in private subnets.
    - The adminServer-vpc has one public subnet in each Az being  divided as 10.20.20.20/25 in eu-central-1a and 10.20.20.128/25 in eu-central-1b giving 128 ip addresses 

- VPC Peering
    - done to connect two vpcs so that they do not have to go over the internet to communicate with each other
    - First a peering connection is defined specifying  the acceptor vpc and connector vpc.
    - In the route table of each of the private subnet of the web servers, an entry is made for the vpc of the admin server
    - Similarly , for the route table of each of the public subnets in the adminServer-vpc, 
    an entry is made for the webServer-Vpc

- Servers
    - The web server is an apache linux server launched in the each private subnet of the Azs  eu-central-1b and eu-central-1a
    - The admin server is a windows server in  eu-central-1b. The RDP and SSH connections are made to the admin server fro the administrator's home or office ip address. To enable SSH connection to the windows server , the OpenSSH is configured to be downloaded at the launch time. The NACL rules had to be modified so as to allow requests to port 443 and 80 and to allow their responses
    
- Security
    - The security group is implemented at instance level
    - The NACLs are implemented at the subnet level

- AutoScaling Group
    - To spin up the instances according to the demand
    - launched in the private subnet of the web server vpc so that they do not have a public ip. They have ony private ip and are accessible via the public dns of the load balancer
    - the desired capacity is set as 2; the min and max being 1 and 3 respectively
    - the user data gets installed on the instances during launch time
    - it was observed that to use the customer managed key to encrypt the ebs volume of asg , the policy statements should include appropriate permissions for both the root user and the role for asg.It was also observed that the default rules were over written and hence the root user should also be included in the policy.
     

- Application Load Balancer 
    - target group consisting of the asg is added to the ALB.
    - performs health check on port 80 of instance for the home page at regular intervals and declares the instances as healthy or unhealthy
    - distributes the traffic accordingly
    - a self signed certificate is configured with the alb so that the user can use https connection with alb. The http connection to port 80 if made is redirected to the port 443 as https.

- KMS key
    - to encrypt the ebs volume of admin server and auto scaled instances
    - the back up vault key
    - S3 bucket

- back up plan
    - to take the back up of the web server instances on a daily basis, retains it for seven days in the back up vault and then deletes it

- S3 bucket
    - to store the user data(post deployment script) scripts and web page related documents

- ACM 
    - to manage and store the created self signed  certificate. 

The architecture diagram for the version 1.1 ia as below

##### ![AWS-architectureDiag-V2](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/projV1.1/architecture-V2.png)
 
   
 




  
   














