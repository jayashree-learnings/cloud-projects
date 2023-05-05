# Design features

The design decisions of the architecture is as follows

The design decisions of the architecture is as follows
 
- VPC  
   - 2 vpcs 
    - webServer-vpc with cidr range cidr range of 10.10.10.0/24. 
    - adminServer-vpc with cidr range of 10.20.20.20/24 
    - Each vpc has 2 Azs(eu-central-1a, eu-central-1b)
    - In each Az of the   web server vpc, there is 2 public subnets of equal cidr range
    - cidr range of public subnets in each vpc is ['10.10.10.0/25', '10.10.10.128/25'] 
    - each subnet of webServer-vpc can have 128 ip addresses 
     - vpc peering is done to establish the connection between the 2 vpcs. First a peering connection is defined specifying  the acceptor vpc and connector vpc. In the route table of the public subnet of the web server, an entry is made for the vpc of the admin server. Similarly , for the route table of each of the public subnets in the adminServer-vpc, an entry is made for the webServer-Vpc.

- Servers
    - The web server is an apache linux server launched in the  public subnet of the Az   eu-central-1a
    - The admin server is a windows server in  eu-central-1b. The RDP connections are made to the admin server fro the administrator's home or office ip address. 
    From the windows admin server the SSH connection is made to the linux web server.
    
- Security
    - The security group is implemented at instance level
    - The NACLs are implemented at the subnet level

- KMS key
    - to encrypt the ebs volume of admin server, web server and the back up vault key


- back up plan
    - to take the back up of the web server instances on a daily basis, retains it for seven days and then deletes it

- boot strap S3 bucket
    - to store the user data(post deployment script) scripts and web page related documents

The architectural diagram is shown below

##### ![AWS-architectureDiag-V2](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/projV1.0/architecture-V1.png)


 
   





