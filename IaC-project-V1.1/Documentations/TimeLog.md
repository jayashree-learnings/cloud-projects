
# Time logs


# Log [19/01/2023]

## One Sentence summary of the day

Tested all the stacks and ensured all are deployed properly


## Challenges

none


## Solutions

none



# Log [18/01/2023]


## One Sentence summary of the day

How to use the jump host server so that there is no need to store the private key in the window server

## Challenges

Showed error on trying to download the openssh in windows server.

## Solutions

Understood that it was because the ports 80 and 443 of the windows server being closed were not allowing for the internet connection.Solved by configuring the SG and NACL appropriately



# Log [17/01/2023]

## One Sentence summary of the day

Started separating the single file into separate stacks


## Challenges

How to use the value of one stack in another


## Solutions

Understood it when I read the documentation of multiple stacks of AWS.


# Log [16/01/2023]


## One Sentence summary of the day

Figured out how to import the certificate using boto3. The stack was deployed and it retrieved the arn. The code creates a certificate if does not exist , else it uses the exiting one


## Challenges

how to use boto3 and its various apis


## Solutions

read the documentation on boto3

# Log [13/01/2023]


## One Sentence summary of the day

Trying to figure out how to create a certificate. Created a separate python file for it and imported the openssl module. 


## Challenges

how to use the open ssl module


## Solutions

understood it by reading the documentation

# Log [12/01/2023]

## One Sentence summary of the day

Tried to figure out how to attach a certificate to alb

## Challenges

reading the related documents

## Solutions

had to understand how to create a ca and to sign the certificate with it

# Log [11/01/2023]


## One Sentence summary of the day

Finished writing the correct policies required for encryption of instances in asg. Deployed and tested it. It was working fine. 


## Challenges

none


## Solutions

none

# Log [10/01/2023]


## One Sentence summary of the day

how to encrypt the ebs volume of  launch template of the asg was a challenge since to use customer managed keys needed the creation of roles and assigning proper permissions.  

## Challenges


The deployment kept on launching multiple servers because of the asg and I had to quit out of the infinite loop manually. The problem was the ebs root volume was not getting attached properly.

## Solutions


Read the documentation on how to encrypt the ebs volume using cmk, added the proper permissions for the root user and also the asg-role. If root user permissions are not defined explicitly, it was observed that it might be overwritten causing the deployment to fail.

# Log [09/01/2023]


## One Sentence summary of the day


Deployed and tested the code with alb and asg. 
## Challenges

None

## Solutions

None

# Log [23/12/2022]


## One Sentence summary of the day

 
Wrote the IaC to provision a basic alb configured on port 80 since using a https connection needed a certificate and I have not reached that far yet.


## Challenges

Had to understand how to do the health checks

## Solutions


Understood it on reading the documentation repeatedly


# Log [22/12/2022]


## One Sentence summary of the day



Deployed the newly added ASG and tested first on port 80.

## Challenges


It was working fine

## Solutions



None



# Log [21/12/2022]

## One Sentence summary of the day



Started working on ASG first

## Challenges


Had to understand how its implemented in code.


## Solutions


Got better understanding



# Log [20/12/2022]



## One Sentence summary of the day



Spent the on understanding about alb and asg

## Challenges



Tried to understand how target groups are added and whats meant by health checks

## Solutions


Understood how they are  implemented



# Log [19/12/2022]



## One Sentence summary of the day



Spent the entire day studying the new requirements

## Challenges



understood new components need to be added

## Solutions



identified the new components for the new design
