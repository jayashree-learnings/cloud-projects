# AWS event bridge

Formerly known as cloudWatch events. It is a serverless event bus that lets you receive, filter, transform, route and deliver events. It increases the user agility, monitor and audit applications, extend functionality with SaaS integrations, customize SaaS with AI/ML.AWS EventBridge provides real-time access to changes in data in AWS services, your own applications and SaaS applications without writing code. It helps to schedule lambda functions, sets event rules as reaction, triggers SQS, SNS etc.  The sources can be ec2 instance starting the instance , S3 object uploading an object and the destination can be lambda, SQS, SNS, step functions, code build etc. The features are 

global end points - this feature enables the automatic failing over their event ingestion to a secondary region without manual intervention.

api destinations - It enables developers to send events back to many on premises or SaaS application. 

archive and reply events - It allows to reprocess ast events back to an event bus. 

schema registry - Event schema is stored in a registry that other developers can easily search and access in the organization.

fully managed and scalable event bus - there is no infrastructure to manage and no capacity to provision.

SaaS integration - It is integrated with SaaS providers like  DataDog, OneLogin 

many built in sources and targets - Over 130 event sources and 35 targets are available

decoupled event publishers and subscribers - applications and micro services can publish events without being aware of subscribers.

event filtering - A single rule can route to multiple targets and they are processed in parallel. 

reliable event delivery - events are stored durably across multiple AZs globally and 99.99% availability is ensured.

automatic response to operational changes in AWS service - It allows to respond quickly to operational changes by writing rules and what action to be taken when an event matches a rule.

scheduled events - Generated on a periodic basis, it invokes target AWS service

monitoring and auditing -  CloudWatch metrics can be used to monitor event bus, cloudWatch logs to store, monitor and analyze events and  CloudTrail to monitor the calls made to EventBridge API

security and compliance - It integrates with IAM, supports with VPC end points, encryption in transit and is GDPR, SOC, DoD etc.

pay per event - Events generated by AWS services are free. Payment is made for events generated by user applications or SaaS integrations.


## Exercise
1. Assignment on event bridge
### Sources
https://aws.amazon.com/getting-started/hands-on/run-serverless-code/?ref=gsrchandson&id=updated

https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/

https://aws.amazon.com/blogs/compute/upgrading-to-amazon-eventbridge-from-amazon-cloudwatch-events/

https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html

https://serverlessland.com/learn/eventbridge

https://cloudacademy.com/blog/aws-eventbridge-features-pricing-and-more/

### Overcome challenges


### Results

python code in lambda

##### ![AWS-EventBridge-lambda-01a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/EventBridge-lambda/01a-lambdaCreated.PNG)

lambda function created

##### ![AWS-EventBridge-lambda-01b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/EventBridge-lambda/01b-lambdaFunction.PNG)


testing lambda

##### ![AWS-EventBridge-lambda-01c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/EventBridge-lambda/01c-lambdaTested.PNG)

rule created 

##### ![AWS-EventBridge-lambda-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/EventBridge-lambda/02a-ruleCreated.PNG)

scheduled for 1 minute

##### ![AWS-EventBridge-lambda-02b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/EventBridge-lambda/02b-scheduledAt1min.PNG)


logs created at one min interval in cloud watch

##### ![AWS-EventBridge-lambda-02c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/EventBridge-lambda/02c-logsAtOne-minInterval.PNG)


