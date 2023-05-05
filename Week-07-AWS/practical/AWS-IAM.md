# AWS IAM(Identity and Access Management) 

Is a service which manage identities and access to AWS services and resources. Using this, we can specify who or what can access services and resources even in  a fine grained scale. IAM can be used to manage users, groups, access policies, roles, user credentials, password policies, MFA, API keys for programmatic access CLI. The user can work with IAM using management console, CLI tools, SDK, IAM HTTPS API.
 

## Key terminologies
IAM role - For the services to perform some actions (eg-for the ec2 to connect with S3), they must be granted permission with IAM roles.

IAM user - people in the organization who has been granted access to AWS account. Each user has 3 main components like a user name. password, permission to access various resources. 

IAM groups - to group people performing similar tasks. Grouping people makes easy to give the permissions to the group rather than assigning permission to each individual

IAM policy - document in json defining the permission of the users.

IAM principal - user/role to which the policy is applied to.It is th person/application that uses AWS root user, IAM user or IAM role to sign in and make requests to AWS.  

IAM resource - list of resources to which allow/deny action is applied to.Can be user, group, policy, role and identity provider objects

root user - the user created by signing in with the email address and password you use to create the account. It has complete admin access

iam identity - IAM resource object used to identify and group. A policy is attached to an IAM identity. They include user, group. role. 

IAM entity - resource objects AWS uses for authentication. Include IAM users and groups.

## Exercise
1. Assignment on IAM

### Sources
https://policysim.aws.amazon.com/home/index.jsp#groups

https://aws.amazon.com/iam/faqs/?nc=sn&loc=5

https://digitalcloud.training/aws-identity-and-access-management/

https://aws.amazon.com/iam/features/analyze-access/?nc=sn&loc=2&dn=1

https://aws.amazon.com/iam/identity-center/?nc=sn&loc=2&dn=2

https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html


### Overcome challenges
Had to understand how a user or another service can access a resource like S3. Understood it when users and resources were created and appropriate permission were given to them.  

### Results

1)Three users were created. A group (cloudengineer-group) was created. All the users were added to the group and the s3 full access policy was attached to the group so that all the members of the group will have full access to the s3 bucket.

##### ![AWS-IAM-user-01a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01a-usersCretedWithPasswd.PNG)

##### ![AWS-IAM-user-01b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01b-GroupCreated-UsersAddedToTheGroup-S3AccessPolicyAttached.PNG)

##### ![AWS-IAM-user-01c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01c-S3FullAccessGiven.PNG)

##### ![AWS-IAM-user-01d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01d-verifyingThedetailsOfAUser.PNG)

##### ![AWS-IAM-user-01e](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01e-UsersInPolicySimulator.PNG)

##### ![AWS-IAM-user-01f](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01f-GroupInPolicySimulator.PNG)

##### ![AWS-IAM-user-01g](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-user-policy/01g-UserViewedInUserPolicy.PNG)


2)A role was created first to give the ec2 instance the full access to s3 bucket. The AmazonS3FullAccessPolicy was attached to the ec2 instance. While launching the ec2 instance, this IAM profile was chosen.In the S3, two buckets were created via AWS management console. The ec2 instance was accessed using ssh protocol and the buckets were listed using the AWS CLI installed in the AWS Linux machine. A third bucket was created using the CLI and it was accessible in the console. It was removed using the CLI commands and the corresponding change was observed in the management console.

creating the role
##### ![AWS-IAM-role-02a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02a-roleCreted.PNG)

permission granted to the role
##### ![AWS-IAM-role-02b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02b-PermissionGrantedToTheRole.PNG)


IAM profile assigned to ec2
##### ![AWS-IAM-role-02c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02c-IAMProfileAssignedToec2.PNG)


access policy in the ec2
##### ![AWS-IAM-role-02d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02d-AccessPolicyInTheec2.PNG)


two buckets created in s3
##### ![AWS-IAM-role-02e](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02e-TwoBucketsCreatedInS3.PNG)


accessing the buckets using aws cli in ec2 
##### ![AWS-IAM-role-02f](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02f-AccessingTwoBktsViaec2.PNG)

creating a new bucket using aws cli
##### ![AWS-IAM-role-02g](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02g-CreatinAndListingNewBkt.PNG)

created new bucket visible in S3 console
##### ![AWS-IAM-role-02h](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02h-BktCreatedInAWScli-VisbleInS3.PNG)

bucket removed via aws cli
##### ![AWS-IAM-role-02i](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02i-BktRemovedViaCLI.PNG)


bucket removal reflected in the console
##### ![AWS-IAM-role-02j](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-07/AWS/IAM-role-policy/02j-BktremovalReflectedInTheConsole.PNG)
