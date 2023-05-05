# AWS config

AWS Config is fully managed cloud-management service meant to assess, audit and evaluate the aws resources.

## Key terminologies
AWS resource - an entity you work with in AWS.

config rule - Is the desired configuration for a resource and is evaluated against configuration changes on relevant resources as recorded by AWS config. The rules can be managed rules(Created by users) or custom rules(predefined customizable rules created by AWS config)   

conformance pack - collection of AWS config rules and remediation that can be deployed as a single entity in an account and a region or across an organization in AWS organizations. 

aggregator - is an AWS config resource type which collects configuration and compliance data from multiple data from multiple AWS accounts and AWS regions into a single account and region. 


### Sources
https://www.youtube.com/watch?v=MJDuAvNEv64

https://aws.amazon.com/config/features/

https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html


https://digitalcloud.training/aws-cloud-management-services/

https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#aws-config-rules


### Overcome challenges


### Results
AWS config is a service which helps to ensure that the resource configurations are efficient, secure and complying with best management practices. The configuration data can be stored into S3 and in case of any non - compliance issues notification can be sent via SNS alerts, cloud watch alarms etc. 

It  helps in 

resource administration - AWS config can be used manage the records of whenever the resources are created, modified or deleted and when it detects that a resource violates the condition, it flags it as a non compliant resource.

auditing and compliance - AWS config provides access to historical configuration of resources which inturn ensures that the data is in compliance with internal policies and best practices. 

managing and trouble shooting configuration changes - AWS config helps to see if the resource intended to be changed is dependent on other resources and assess the impact of the change.  
 
security analysis - AWS config helps to view IAM policy attached to IAM user, group or role at any time, security groups of ec2 instances etc.  
 


