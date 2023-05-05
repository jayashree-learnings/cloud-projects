# AWS Security Groups and NACLs

Both security groups and NACL(network Access Control List) are a part of firewall meant for providing security to the resources  by controlling inbound and outbound traffic. Security group controls the traffic at the instance level. NACL works at the subnet level.

## Key terminologies
NACL - Network Access Control List.

ingress traffic - inbound traffic

egress traffic - outbound traffic

## Exercise
1. Security Groups in AWS 
2. Network Access Control Lists in AWS
 
### Sources
https://www.geeksforgeeks.org/amazon-web-services-security-group-vs-nacl/

https://www.javatpoint.com/aws-nacl-vs-security-group

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html


### Overcome challenges

Had to understand the functionality and specific need for two types of firewalls. 

### Results
1) Security Groups 

- Operates at the instance level.

- Supports allow rules only.

- Stateful - return traffic automatically allowed, regardless of any rules.

- all rules evaluated before deciding whether to allow traffic

- by default, it denies all inbound traffic and allows all outbound traffic


2) Network Access Control Lists - 

- operates at the subnet level

- supports allow and deny rules

- stateless - return traffic must be explicitly allowed by rules.

- rules processed in number order when deciding whether to allow traffic.

- by default denies both inbound and outbound traffic.















