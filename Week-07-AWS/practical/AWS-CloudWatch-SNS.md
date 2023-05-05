# AWS CloudWatch

AWS cloudWatch is a performance monitoring service which can be used to track metrics, collect and  monitor log files and set alarms. It can be accessed via API, CLI, SDK and management console. It helps to monitor resources like ec2 instances, dynamo db table, RDS DB instances, custom metrics generated by applications and services. 
 

## Key terminologies
Logs - records what happened and includes examples like for lambda, it is function logs, for ECS , it is the collection from containers.

Alarms - Used to trigger notification for the metric

metrics - is a variable which is monitored and has time stamp. eg - CPU utilization, bucket sizes, service limits

events - stream of events describing changes in the AWS resources

## Exercise

1. Assignment on CloudWatch

### Sources

https://digitalcloud.training/aws-monitoring-and-logging-services/

https://www.youtube.com/watch?v=-rQku_AeN_Y

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_AlarmAtThresholdEC2.html

https://arstech.net/install-stress-on-amazon-linux/

### Overcome challenges


### Results


1)A cloudwatch alarm to monitor the ec2 instance's CPU utilization was set up in integration with SNS. First an ec2 instance was launched with basic configuration.A topic was created in SNS and subscription was added with email protocol. The email subscription was confirmed from my end. In cloudwatch, an alarm was created for the ec2 instance (pre instance category) when average cpu utilization exceeds 50 and in the action, sns notification was set up. To increase the cpu load, ssh connection was made to the ec2 instance, epel and stress packages were installed and  linux command stress was used. The cpu utilization graph in the cloudwatch alarm reflected the changed CPU load. The email was sent to my account giving warning about the changed cpu utilization. 


ec2 launched with basic configuration

##### ![AWS-cloudwatch-sns-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/01-ec2LaunchedWithBasicConfigurations.PNG)


topic created in email protocol and email added to subscription  

##### ![AWS-cloudwatch-sns-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/02-TopicCreatedInEmailProtocolSubscriptionAddedAndConfiremedByThatPerson.PNG)

creating the alarm

##### ![AWS-cloudwatch-sns-03a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/03a-AlarmCreated.PNG)

actions enabled in the alarm

##### ![AWS-cloudwatch-sns-03b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/03b-actions.PNG)

installing epel

##### ![AWS-cloudwatch-sns-04a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/04aepelInstall.PNG)


installing stress

##### ![AWS-cloudwatch-sns-04b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/04b-StressInstall.PNG)

stressing the ec2

##### ![AWS-cloudwatch-sns-04c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/04c-stressing-ec2Instance.PNG)


cpu utilization greater than the threshold in ec2 console
##### ![AWS-cloudwatch-sns-05a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/05a-CPU%25gretaerInec2Console.PNG)

cpu utilization greater than the threshold in cloudwatch 

##### ![AWS-cloudwatch-sns-05b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/05b-CPUExceededInCloudWatch.PNG)

history of alarm

##### ![AWS-cloudwatch-sns-05c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/05c-historyOfalarm.PNG)

email notification to the given mail id

##### ![AWS-cloudwatch-sns-05d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/CloudWatch-SNS/05d-EmailNotification.PNG)




