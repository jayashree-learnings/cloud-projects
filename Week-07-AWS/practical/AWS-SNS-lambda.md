# AWS SNS-lambda

AWS Simple Notification Service (SNS) is an application integration web service which helps to set up, operate and send notifications from the cloud. It follows the publish - subscribe messaging paradigm  where the notifications being pushed to the clients. Notifications can be manual or automated. It supports event notification, monitoring applications, mobile applications. Being a pay-as-yuo-go model, it has no upfront costs and data type is json. It is a flexible message delivery system over multiple transport protocols. 

AWS lambda is a serverless computing service and executes the code only when needed. The payment is done when the code is executed. The benefits include no servers to manage, continuous scaling, millisecond billing, integration with other AWS services. Lambda supports languages like python, ruby, java , C#, Go and powershell. 
 

## Key terminologies
topic - how you label and group different end points that you send messages to

subscriptions - the end points that a topic sends messages to. Can be HTTP, HTTPS, email, lambda etc

publishers - the person or alarm or event that gives SNS the message that needs to be sent.

serverless compute - the user neednot have to provision and manage servers and it features auto scaling, high availability, paty for use billing model.

run time - provides a language specific environmment that runs in an execution environment.

lambda handler - Is the method in the function code that processes events

concurrency - the number of requests the function serves at a given time

event payload - a json structure containing arrays and nested elements.

execution role - gives permission to upload logs and access other AWS services. 

function policy - gives other services the permission to invoke lambda

trigger - resource or configuration that invokes a lambda function. 

handler function - function to be executed upon invocation

event object - data sent during lambda function invocation

context object - methods available to interact with run time information (request id, log group)

event driven computing - subscriber performs work in response to events triggered by publisher  services. 

## Exercise

1. Assignment on SNS-lambda

### Sources

https://aws.amazon.com/getting-started/hands-on/run-serverless-code/?ref=gsrchandson&id=updated

https://aws.amazon.com/sns/faqs/

https://aws.amazon.com/sns/features/

https://digitalcloud.training/aws-compute-services/

https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html#gettingstarted-concepts-runtime

https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html

https://docs.aws.amazon.com/lambda/latest/operatorguide/payload.html

### Overcome challenges

Had to understand how SNS can be integrated with lambda. Understood it when SNS trigger was used as  trigger to invoke the lambda function.

### Results

1)The hands-on tutorials on lambda-SNS were done to gain insights into those services. A SNS trigger was used to invoke the lambda. First a SNS topic was created. A lambda function which prints the incoming event was created by modifying the default code and deployed. The lambda function was added to the SNS topic subscription so that when ever a  new message is published to the topic, it invokes the lambda function. The trigger was reflected in the lambda dashboard. A new message in json format was published to the topic. To see if it has triggered the lambda function, the cloudWatch logs were examined.  

In the next stage, the code was modified to print the sum of 2 numbers(2 and 3) instead of printing the event and deployed. A new message was published to the same topic and the cloud watch log was checked again. This time it printed the sum as 5 in the log.

topic created in sns

##### ![AWS-SNS-lambda-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/01-SNSTopicCreated.PNG)

lambda function created

##### ![AWS-SNS-lambda-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/02-lambdaFunctionCreated.PNG)


lambda subscription added to sns topic

##### ![AWS-SNS-lambda-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/03-lambdaSubscrptionAddedtoSNStopic.PNG)

trigger added to lambda console

##### ![AWS-SNS-lambda-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/04-TriggerAddedToLambdaConsole.PNG)

publishing message to topic

##### ![AWS-SNS-lambda-05](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/05-publishMsgToTopic.PNG)

cloud watch logs

##### ![AWS-SNS-lambda-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/06-CloudWatchLogs.PNG)

code modified to display sum

##### ![AWS-SNS-lambda-07a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/07a-codeModifiedToGetSum.PNG)

sample message published

##### ![AWS-SNS-lambda-07b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/07b-sampleMsgPublished.PNG)

sum printed

##### ![AWS-SNS-lambda-07c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/07c-CloudWatchLogGroup.PNG)

cloud watch log group
##### ![AWS-SNS-lambda-08](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-lambda/08-PrintedTheSum.PNG)