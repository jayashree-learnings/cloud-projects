# AWS Shared Responsibility Model

AWS and the customer shares the security and compliance of the cloud architecture model.While AWS is responsible for the security of the cloud, the security inside the cloud is solely the responsibility of the customer.

## Key terminologies
IaaS - In this service model, the customer manages from the virtual server upwards and AWS manages the underlying infrastructure.

PaaS - A type of service model in which customer is responsible for the code and data and the underlying facilities managed by AWS

SaaS - A type of consumption service model where everything is managed by the AWS and the customer has the least responsibility and least control.


## Exercise
1. Study the AWS Shared Responsibility Model
 
### Sources

https://aws.amazon.com/compliance/shared-responsibility-model/

https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/shared-responsibility-model.html


### Overcome challenges
Had to understand what are the responsibilities of the customer and what will be AWS responsible for while adopting a cloud infrastructure.


### Results

1)The shared responsibility model was studied which outlines what the AWS is responsible for and what customers are responsible for while adopting a cloud infrastructure.
The shared responsibility model is applicable in the case of both services and iT controls.In the case of services, the responsibility shared between AWS and customers depends on the type of the service like IaaS, SaaS and PaaS.  In the case of controls, some types are 

Inherited controls - Physical and environmental controls which a customer fully inherits from AWS

Shared controls - here AWS provides the requirements for the infrastructure and customer must provide their own control implementation. For eg, in patch management, AWS patches the flaws in the infrastructure, but customers should patch their OS.In the case of configuration management, AWS configures the infrastructure, but customer must configure their own OS, DB and application. For awareness and training programs, AWs trains their employees, but a customer has to train their own employees.

##### ![AWS-09-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-06/SRM/SRM-01.png)















