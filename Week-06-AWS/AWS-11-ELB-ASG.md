# AWS ELB and ASG
AWS ElasticLoadBalancer(ELB) -  Distributes the incoming load to various targets across multiple AZs. The 4 main types are

Application Load Balancer - Used to load balance the http/https requests and it works in the layer 7 of the OSI model.

Network Load Balancer -Used for low latency, high performance applications and it works in the layer 4 of the OSI model using TCP UDP protocols.

Gateway Load Balancer - Used when it is required to run and deploy third party virtual appliances. It routes the traffic to a third party application for monitoring the packet after which it routes the traffic to the main application like a NLB. It thus acts on the layers 3 and 4 of the OSI stack. 

Classic load balancer - BEing an outdated service, it is recommended not to use this service. It supports the instances with any OS currently supported by Amazon EC2 service.

AWS Auto Scaling Group(ASG) - Eliminates the need for guessing the capacity beforehand which is extremely useful for a high fluctuating traffic. The common practice is to host the application in a fleet of servers than a single server. The number of services can be increased or decreased automatically with the help of auto scaling group. 

## Key terminologies
Horizontal scaling - The number of machines of the similar capacity are increased or decreased.

vertical scaling - The capacity of the single instance is increased or decreased.

scale out - increase the number of instances.

scale in - decrease the number of instances.

## Exercise
1.Launch an EC2 instance with the following requirements:
○ Region: Frankfurt (eu-central-1)
○ AMI: Amazon Linux 2
○ Type: t3.micro
○ User data:
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
○ Security Group: Allow HTTP
● Wait for the status checks to pass.
● Create an AMI from your instance with the following requirements:
● Image name: Web server AMI

2.Create an application load balancer with the following requirements:
○ Name: LabELB
○ Listener: HTTP on port 80
○ AZs: eu-central-1a and eu-central-1b
○ Subnets: must be public
○ Security Group:
■ Name: ELB SG
■ Rules: allow HTTP access
○ Target Group:
■ Name: LabTargetGroup
■ Targets: to be registered by Auto Scaling

3.Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.Create an auto scaling group with the following requirements:
○ Name: Lab ASG
○ Launch Configuration: Web server launch configuration
○ Subnets: must be in eu-central-1a and eu-central-1b
○ Load Balancer: LabELB
○ Group metrics collection in CloudWatch must be enabled
○ Group Size:
■ Desired Capacity: 2
■ Minimum Capacity: 2
■ Maximum Capacity: 4
○ Scaling policy: Target tracking with a target of 60% average CPU utilization

4.Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
● Access the server via the ELB by using the DNS name of the ELB.
● Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.

 
### Sources
https://aws.amazon.com/elasticloadbalancing/

https://docs.aws.amazon.com/AmazonECS/latest/userguide/load-balancer-types.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html

https://www.youtube.com/watch?v=UPDMso_4O5A/

### Overcome challenges
Had to understand how load balancer distributes the load by redirecting the traffic coming to the instances so that load on a particular instance does not exceed certain limits. Understood that when used in combination with ASG, the instances can be scaled in or scaled out depending on the load. 

### Results
1)The ec2 instance was launched as per the given requirements. By checking the public DNS name of the server it was verified that it is working fine. An AMI was created from the above instance
##### ![AWS-11-01a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/01a-ec2launch.PNG)

##### ![AWS-11-01b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/01b-ec2runningproperly.PNG)

##### ![AWS-11-01c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/01c-CreatedAMI.PNG)



2)An application load balancer was created with the given requirements to handle the http requests. The ELB was placed in the two default public subnets as it is internet facing. for the security group of ELB, it was opened to the public at port 80. The target group was created, but the instances were not registered as it would be done automatically by the auto scaling group.

##### ![AWS-11-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/02a-LoadBalancer.PNG)


##### ![AWS-11-02b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/02b-TargetGroupCreatedbutNotargets.PNG)


##### ![AWS-11-02c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/02c-ELBCreatedInPublicSubnets.PNG)

3)First a launch template was configured for the auto scaling group in which the templates of the instances were specified. The previously created AMI was chosen and configuration done for the same. Here for the security group, port 80 was opened only for ELB by choosing custom ip and selecting the security group id of the ELB(default ip of VPC also can be given). Thus it was not opened to the entire public. Then the auto scaling group was configured to be in the public subnets of the AZs and elastic load balancer was added to it. The health check was chosen for ELB. The scaling policy was set to 60% of the CPU utilization so that when load is more, it creates new instances automatically.

S.G. of launch template allowing only the traffic from the ELB

##### ![AWS-11-03a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/03a-SGOfLaunchTemplateAllowsOnlyELBtraffic.PNG)

creating launch template 
##### ![AWS-11-03b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/03b-LaunchtemplateCreated.PNG)


ASG creation
##### ![AWS-11-03c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/03c-ASGCreated.PNG)

Two instances created by ASG
##### ![AWS-11-03d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/03d-twoInstancesCreatedBYASGIn2AZs.PNG)


Public DNS of ELB
##### ![AWS-11-03e](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/03e-publicDNSofELB.PNG)


Access web server via public dns of ELB
##### ![AWS-11-03f](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/03f-oneWebServerAccessedViaELBpublicDNS.PNG)

4)Finally the application was accessed by using the DNS of the ELB. The ip addresses of the individual servers was not used to access it. The ELB being internet facing had the http allowed from outside in its security group. The individual servers had traffic coming from the ELB configured in their security group and they no traffic from outside was allowed into them. 
After accessing the web page, the load test was done by clicking on the tab and the load of CPU thus increased. It was verified that the autoscaling policy launched two more instances to cater to the extra CPU load.

increasing the cpu load

##### ![AWS-11-04a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/04a-CPUIncreaed.PNG)


two more instances created

##### ![AWS-11-04b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/AWS-11/04b-TwoMoreInstancescreatedByASG.PNG)








