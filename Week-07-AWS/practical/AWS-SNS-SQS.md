# AWS SQS

AWS Simple Queue System (SQS) is a message queue service used by distributed applications to exchange messages through a polling model. It is a temporary repository for messages that await processing. The use cases include
increase application reliability and scale, decouple microservices and process event-driven applications, ensure work is completed cost effectively and on time, maintain message ordering with deduplicate messages. 

## Key terminologies

standard queue - Supports unlimited number of transactions and supports at least-once delivery

fifo queue - first in first out queue supports up to 300 messages per second. For a batch of 10 messages, it supports 3000 messages per second. Duplicates are not introduced and message remains available till the consumer processes and deletes it. 

## Exercise
1. Assignment on SNS,SQS
### Sources
https://aws.amazon.com/getting-started/hands-on/run-serverless-code/?ref=gsrchandson&id=updated

https://aws.amazon.com/getting-started/hands-on/send-fanout-event-notifications/

https://aws.amazon.com/blogs/compute/upgrading-to-amazon-eventbridge-from-amazon-cloudwatch-events/

https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html

### Overcome challenges

Had to understand how the SNS-SQS integration works. Understood it when implementing the two services together.

### Results 

1)The hands-on tutorials on SNS,SQS were done to gain insights into those services. In the selected region, a SNS topic (New Orders) was created in the basic standard format.Two SNS queues(Inventory queue and Analytics queue) were created with basic configurations. The two queues were subscribed to the topic so that whenever a new message is published to that topic, both the queues receive notification. The message was published to the new orders topic. In the SQS dashboard, each queue was selected and the messages were polled. The message details were visible in each of the queues. 


topic created in sns dash board

##### ![AWS-SNS-SQS-01a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01a-CreateTopic.PNG)

two queues created with basic configuration

##### ![AWS-SNS-SQS-01b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01b-TwoQueuesCreatedWithBasicConfigurations.PNG)

queue subscribing to the topic

##### ![AWS-SNS-SQS-01c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01c-queueSubscribingToTopics.PNG)


subscriptions confirmed in the sns dashboard

##### ![AWS-SNS-SQS-01d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01d-TwoSubscriptionsConfirmedInSNSDashboard.PNG)

message published to the topic

##### ![AWS-SNS-SQS-01e](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01e-publishMsgToTopic.PNG)

two messages available as two messages were published 

##### ![AWS-SNS-SQS-01f](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01f-TwoMsgAvailableAsTwoMsgsPublishedToTopic.PNG)

polling the messages 

##### ![AWS-SNS-SQS-01g](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01g-msgsVisibleAfterPolling-AnalyticsQueue.PNG)

details of the  message in analytics queue

##### ![AWS-SNS-SQS-01h1](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01h1-detailsVerifiedForFirstMsg-AnalyticsQueue.PNG)


details of the message in inventory queue

##### ![AWS-SNS-SQS-01i](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/SNS-SQS/01i-detailsOfMsg-InventoryQueue.PNG)

