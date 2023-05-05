#  AWS EC2

Amazon elastic cloud computing(ec2) is an AWS service that produces scalable computing capacity in the cloud. The features of ec2 include AMI which is a pre configured templates for the instance, key pairs to enable the user to securely ssh into the system, instance store volume for temporary data that gets deleted when you stop or terminate the instance, persistent storage volume which is the Elastic Block Storage (EBS), regions and availability zone which are physical locations for the resources, firewall which helps to specify the access rules for the resources, IPV4 addresses, tags to identify resources, VPC (Virtual Private Cloud) to logically isolate network to provision the resources securely and instances. The types of instances are

- general purpose - Mostly used for web servers where there is balance between storage, memory and computing.

- memory optimized - Used for cases that process large data sets in memory. Used for in-memory databases for BI, relational/non relational databases etc.

- compute optimized - Used for high compute intensive purposes. Used for gaming servers, HPC(High Performance Computing), batch processing workloads etc.

- storage optimized - Used where frequent read/write access to data sets on local storage. Used for OLTP systems, data ware housing , distributed file sysytems etc.


## Key terminologies

on-demand instance - You pay for the compute capacity you use.

spot instance - Used when you have workloads that can be interrupted.

reserved instance - When your application is used steadily, you can reserve for 1 to 3 year.

dedicated host - A physical server is fully dedicated to run your instances. 

dedicated instance - instance run on hardware that is dedicated to you.

savings plan - It is based on the actual compute usage measured per hour for 1 to 3 years. 


## Exercise
1. Navigate to the EC2 menu. Launch an EC2 instance with the following requirements:

    - AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type

    - Instance type: t2.micro

    - Default network, no preference for subnet

    - Termination protection: enabled

    - User data:

        #!/bin/bash

        yum -y install httpd

        systemctl enable httpd

        systemctl start httpd

        echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html

    - Root volume: general purpose SSD, Size: 8 GiB

    - New Security Group:

        Name: Web server SG

        Rules: Allow SSH, HTTP and HTTPS from anywhere

Exercise 2

- Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.

- Log in to your EC2 instance using an ssh connection. 

- Terminate your instance.
 
### Sources

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html

https://aws.amazon.com/ec2/pricing/

### Overcome challenges

### Results
1) An ec2 instance with the above requirement was launched in AWS. In the user data, a script for enabling apache2 web server was given so that it started automatically when the system is booted up. A new security group was created allowing http, https and ssh in the inbound traffic. A key pair was generated which was used to ssh into the server. Once ec2 was launched, it showed that it passed the two checks of system reachability and Instance reachability was checked. By giving http://public-ip in the web browser, the test web page of apache2 was accessible.

    choosing t2-micro 
    ##### ![AWS-05-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/01-AMI-t2-micro.PNG)


    S.G enabled
    ##### ![AWS-05-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/02-C2-SG.PNG)


    user data
    ##### ![AWS-05-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/03-Userdata.PNG)


    reliability check 
    ##### ![AWS-05-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/04-ec2-reliabilityChecks.PNG)


    access apache2
    ##### ![AWS-05-05](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/05-Apache2Access.PNG)


2) For logging into the above ec2 instance, a tool called mobaxterm was made use of. When the command whoami is typed, it shows the user name. The correct private ip of the ec2 machine was also displayed.

    ssh into server
    ##### ![AWS-05-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/06-SSHintoServer.PNG)



    terminate ec2
    ##### ![AWS-05-07](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-06/07-terminate-ec2.PNG)

















