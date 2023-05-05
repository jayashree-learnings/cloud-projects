# AWS File, AppSevices, CDN, DNS,DB
AWS offers a variety of services related to areas like the file system (EFS), application services (ElasticBeanStalk), Content Delivery Network(CloudFront), Domain Name System (Route 53), Data Bases(RDS/Aurora). 

## Key terminologies

end point - URL of the entry point for an AWS web service

domain name - the name the user enters in the browser to display the web site

aurora cluster - one or more DB instances and a cluster volume that manages the data for those DB instances.

point of presence - Used to deliver content to end users at high speeds for reduced latency.

Elastic File System (EFS) - Is a network file system mountable on many ec2 instances simultaneously with no set up fee. It is a serverless set and forget file system which is ideal for storage classes that need high durability and availability.Suitable for big data and analytics, web serving, content management etc. 

AWS RDS - Fully managed relational data service supporting mysql, PostgreSQL, MariaDB, SQL Server etc. It  also supports set up in multi AZ for disaster recovery, vertical and horizontal scaling, EBS backed storage etc. 

AWS Aurora - A fully managed relational database service which supports both mySQL and Aurora DB.It is highly available , fault tolerant and self healing storage system that has 15 low-latency read replicas, point in time recovery, continuous back up of Amazon S3 and replications across 3 AZs. It costs more than the RDS but is more efficient.


## Exercise
1. Study ElasticBeanStalk, CloudFront, Route53

2. Assignment on EFS, RDS, Aurora
 
### Sources

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html

https://aws.amazon.com/rds/aurora/

https://aws.amazon.com/elasticbeanstalk/

https://aws.amazon.com/getting-started/tutorials/create-network-file-system/?pg=ln&sec=hs

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.html#CHAP_Tutorials.ThisGuide

https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html

https://aws.amazon.com/cloudfront/

https://aws.amazon.com/route53/

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html

https://aws.amazon.com/getting-started/hands-on/create-high-availability-database-cluster/#

https://aws.amazon.com/getting-started/hands-on/building-serverless-applications-with-amazon-aurora-serverless/

https://aws.amazon.com/getting-started/hands-on/migrate-rdsmysql-to-auroramysql/

https://docs.aws.amazon.com/efs/latest/ug/installing-amazon-efs-utils.html

https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html


### Overcome challenges
Had to look up on how the AWS offers services in each of the different fields like file system, caching content, resolving the domain name to ip addresses, how to manage data bases and how to deploy applications quickly to cloud.


### Results
1)The services like Elastic Beanstalk, CloudFront and Route53 were studied. 

ElasticBeanStalk - Is a PaaS service intended to deploy applications on AWS with full control over configuration. Payment is done for the underlying infrastructure. It supports many platforms like python, go, single/multi container docker. When an application is deployed, it works with other services like ec2 to configure servers, S3 for storage purpose, cloud watch for monitoring the health, CloudFormation for provisioning the infrastructure. 

CloudFront - Is a CDN network.The purpose of cloudfront is to replicate the resources to the AWS edge locations and to cache the requests resulting in low latency and thus enhancing the user experience. When a user wants to access a website, The DNS routes the request to the CloudFront POP. The CloudFront checks its cache for the requested object and if it is available, it returns to the user. If not, CloudFront redirects the request to the origin server which sends the object back to the edge location. It then adds this object to its cache for the next time some one requests it. 

Route53 - Is a DNS(DDomain Name System) service. It translates the domain names to IP addresses. It can be combined with health checking services to route the traffic to healthy resources. Its globally distributed nature makes it highly available and low latent. The routing policies are simple routing policy (a single resource that performs a given function for your domain),fail over routing policy(when configuring active passive fail over), geo location routing policy(routing based on location of users), geo proximity routing policy (when traffic is routed based on location of resources and optionally shift traffic from resources in one location to another resources in another), latency routing policy (when resources are available in multi-AZs and traffic is routed to regions of the lowest latency), IP based routing policy (when traffic is routed based on the location of the  users and have the i.p. addresses that traffic originates from ) , multi-value answer policy (when route 53 is expected to respond to DNS queries), weighted routing policy (use to route traffic to multiple proportions that you specify). After registering the domain name with route 53, a hosted zone with 4 server names is assigned and at the end of the registration process, information is sent to the registrar who in turn sends the information to the registry. The registry stores the information in their own database and in the public WHOIS database.  

2)The hands-on tutorials on EFS, RDS and Aurora were done to gain insights into those services.

a) Two ec2 instances were launched in 2 different AZs and  a security group allowing NFS and ssh protocol. An EFS file system was created in which 3 AZs were selected a the mount points. In both the  ec2 instances, the nfs-utils were installed, a directory was created and mounted. Three files were created in one instance and they were accessible in the second instance.  

S.G. of the instances
##### ![AWS-13-EFS-00](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/EFS/00-SGOfec1-AZ1a.PNG)

Two instances launched
##### ![AWS-13-EFS-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/EFS/01-LaunchTwoInstancesIn2AZs-WithNFS-SG.PNG)

3 AZs chosen for mount point targets
##### ![AWS-13-EFS-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/EFS/02a-ChooseEFS-SGIN3AZs.PNG)

EFS created
##### ![AWS-13-EFS-02b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/EFS/02c-EFSCreated.PNG)

Mounting and file creation in one instance
##### ![AWS-13-EFS-03a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/EFS/03a-efs-instance01-3filesCreated.PNG)

Mounting and file accessing in second instance
##### ![AWS-13-EFS-03b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/EFS/03b-3filesaccessibleInserver.PNG)


b) An AWS aurora was created with no-replica option. The writer instance was created in AZ-1b. A reader replica was explicitly created in AZ-1c and it was set to tier zero for fail over priority. The writer instance was failed. After a few seconds, reader and writer instance was interchanged. The replica thus became the primary instance.  

No replication option chosen
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/01-NoReplicaOptionChosen.PNG)

Writer instance created 
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/02-WriterinstanceInAZ1b.PNG)

reader instance was created
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/03-readerInstanceCreated-tierzerowassetduringcreation-AZ1aChosen.PNG)

Writer instance fail over
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/04-FailWriterInstance.PNG)

Reader and writer instances exchanged
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/05a-ReaderAndWriterInterchanged.PNG)

Logs of current reader instance 
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/05b-LogofCurrentReaderInstance.PNG)

Logs of current writer instance
##### ![AWS-13-Aurora-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/Aurora/05c-LogOfCurrentWriterInstance.PNG)

c)An ec2 instance was launched in the default VPC(eu-central-frankfurt) in AZ-1b. A RDS of mySQL support engine was launched in AZ-1a and security group was attached to it. A sample database name (studentdb) was specified during the launch of the RDS instance . In the security group, in the inbound rule mySQL/Aurora was chosen as the type which has default port of 3306 and in the source type custom ip was chosen and the private ip of the ec2 instance was given. The ec2 instance was accessed via mobaxterm (SSH protocol) and mySQL was installed. In the CLI, appropriate linux command was given to connect with the mySQL instance which uses the username, password and end point of the DB instance. The sample database could be seen after connecting to it and a table was created in the same database to insert some values. 

creating mySQL RDS
##### ![AWS-13-RDS-01a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/01a-mySQL-RDS-Created.PNG)

SG of the RDS
##### ![AWS-13-RDS-01b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/01b-SGOfmySQLRDS.PNG)

ec2 instance in the same VPC
##### ![AWS-13-RDS-01c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/01c-ec2InSameVPC.PNG)

Installing mySQL in the ec2 instance
##### ![AWS-13-RDS-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/02a-installmysql.PNG)

Displaying the studentdb and creating table
##### ![AWS-13-RDS-02b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/02b-enteringmySQL-displayStudentdb.PNG)

inserting values into the table
##### ![AWS-13-RDS-02c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/02c-valueInsertion.PNG)

sample query
##### ![AWS-13-RDS-02d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/RDS/02d-samplequery.PNG)
