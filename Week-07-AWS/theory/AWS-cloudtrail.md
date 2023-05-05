# AWS cloudtrail

AWS cloud trail is a logging and monitoring service which saves the api call in an account and enables auditing, security monitoring and operational troubleshooting in the account.  

## Key terminologies

management event - it captures control plane actions on resources like creating or deleting S3 bucket.  

data event - capture data plane actions like with in a resource like reading or writing S3 object. 
  

### Sources
https://digitalcloud.training/aws-monitoring-and-logging-services/

https://aws.amazon.com/cloudtrail/faqs/

https://aws.amazon.com/cloudtrail/features/

https://www.youtube.com/watch?v=mXQSnbc9jMs


### Results

AWS CloudTrail logs, continuously monitors and retains account activity related to actions across AWS infrastructure and records them as events. It helps to answer the questions like who did what and where . It is by default set as on for all accounts and uses 3 event-features- event history(90 day history of control plane actions at no extra charge), cloud trail lake(managed data lake for user and API activity) and trails (a record of account activities storing them in S3 and optionally storing in CloudWatch Logs and EventBridge). Some of the features are 

- always on - It is enabled on all accounts and records management events 

- storage and monitoring - logs can be stored in S3 or cloud watch logs.

- immutable and encrypted activity logs - validity of cloudtrail logs can be verified by log file integrity validation.

- insights and analytics - SQL queries, cloudtrail insights can be enabled in cloudtrail to audit and gain insights.

- multi - region - events from multi-regions in a single location can be captured and stored.

- multi-account - logs from multi accounts in a single location can be collected and analyzed. 

It logs the API calls made via management console, CLi tools, higher AWS services(CloudFormation) and SDK.It thus helps to 

- maintain compliance, improve security, consolidate activity across all regions

- provides visibility into the account

- helps to track the changes and trouble shoot operational issues



