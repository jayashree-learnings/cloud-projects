# AWS Dynamo DB
AWS DynamoDB is a fully managed NoSQL database which can scale to massive workloads and is serverless service. It supports key-value and document data models. DynamoDB is made up of tables, items and attributes. It can scale more than 10 trillion requests per day with peaks greater than 20 million requests per second over petabytes of storage. It provides very low latency and data is replicated in 3 geographically distributed locations to enable high availability and data durability.       

## Key terminologies

tables - a collection of items

item - comparable to  rows in a relational DB and is a collection of attributes.

attribute - are columns and consists of a name and a value or values


## Exercise
1. Assignment on DynamoDB
### Sources
https://aws.amazon.com/getting-started/hands-on/create-nosql-table/

https://aws.amazon.com/dynamodb/getting-started/#Learning_path.3A_Using_DynamoDB_and_AWS_Lambda_in_your_serverless_applications

https://aws.amazon.com/dynamodb/

https://digitalcloud.training/amazon-dynamodb/


### Overcome challenges


### Results
First a dynamo-db table(students-details-db) was created. Then a role by the name LambdaToDynamoDBAndCloudWatch-role was created and two policies (AmazonDynamoDBFullAccess, CloudWatchFullAccess) which gives the lambda function the full access to dynamodb and cloudwatch were attached. A lambda function(InsertDataToDynamoDB) was created in python to insert values to dynamoDB and the new role was attached to it. 
The function was tested by passing the attributes like student_id, student_name, dept in json format for the first item and for the second item additional attribute of place was added. These two records wer available in the students-details-db table.


table created in dynamo DB

##### ![AWS-dynamodb-lambda-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/01-DynamoDBCreated.PNG)

policies attached to the lambda role

##### ![AWS-dynamodb-lambda-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/02-LambdatoDynamoDbAndcloudWatch-role.PNG)

lambda created and role is assigned

##### ![AWS-dynamodb-lambda-03a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/03a-LambdaCreatedAndAssignedTheRole.PNG)

code in the lambda function

##### ![AWS-dynamodb-lambda-03b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/03b-LambdaFunction.PNG)

test event of one record

##### ![AWS-dynamodb-lambda-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/04-testEvent.PNG)

message after testing the function

##### ![AWS-dynamodb-lambda-05a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/05a-messageAfterInsertionTesting.PNG)

values inserted into the table

##### ![AWS-dynamodb-lambda-05b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/05b-ValuesInserted.PNG)

cloud watch logs created

##### ![AWS-dynamodb-lambda-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/dynamodb-lambda/06-CloudWatchLogs.PNG)



