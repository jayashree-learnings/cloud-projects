# AWS ECS

AWS elastic container service (ECS) is a computing service. It enables the application portfolio to grow from a single docker container depending on the requirement.

## Key terminologies

docker - A docker container image is a light weight stand alone executable package that includes everything to run the code-code, run time, system tools, libraries etc. 

container - A standard unit of software that packages up code and all dependencies which helps to run the application irrespective of the environment. 

ECS cluster - grouping of tasks or services. 


### Sources

https://aws.amazon.com/ecs/faqs/#General

https://digitalcloud.training/aws-compute-services/#amazon-elastic-container-service-ecs

https://aws.amazon.com/ecs/features/

https://www.docker.com/resources/what-container/




### Results
AWS ECS is a container management service that supports docker containers. It allows to easily run applications on a managed cluster of ec2 instances. It is possible to launch and stop container based applications, query the complete state of your cluster, access features like security groups, ELB, EBS and IAM with the help of API calls. It is possible to use ECS or any third party applications to schedule container placement across the cluster depending on the needs.  

- ECS eliminates the need to install, operate and scale down the cluster management of your organization. 

- ECS lets you schedule application, services and batch processes using containers.

- ECS maintains application availability by allowing the scaling of containers.

The key features of ECS are

- AWS Fargate is a Serverless container management so that the users don't have to worry about managing servers, capacity planning and also about its security and isolation. 

- ECS anywhere - It   helps to use the ECS console and operator tools to manage on-premises container work loads. AWS System Manager(SSM) helps the integration between the on-prem hardware and AWS control pane. 

- Security and isolation by design - ECS has security, identity, management and governance tools and granular permission can be assigned to each of the containers.  

- autonomous control plane operations - ECS is a fully manged container orchestration service with AWS configuration and operational best practices built-in, allowing the users to focus on building the applications and not the environment. 



