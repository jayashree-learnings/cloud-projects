#  AWS Global Infrastructure
AWs has data centres located throughout the globe consisting of a total of  27 launched regions, 87 availability zones with each AZ consisting of a minimum 2 data centres. 

## Exercise

● What is an AWS Availability Zone?

● What is a Region?

● What is an Edge Location?

● Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).
 

### Sources
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html

https://aws.amazon.com/about-aws/global-infrastructure/

https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/

https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/

### Overcome challenges

Had to understand what are the factors considered while choosing a region to launch resources. 

### Results
1) Availability zone - An availability zone consists of one more data centres. Located with in  a region , they are isolated locations. Each AZ has independent power, cooling, physical security so that if 1 AZ goes out of service, others should not be impacted. 

2) Region - It is a physical location in the world and is independent. Each region is a separate geographic area.

3) Edge Location - The main purpose of edge locations is to reduce the latency by caching the content. Some of the services which use edge locations are cloud front, route 53, web application firewall and aws shield.  

4) The choice of one location over the others depend on

- Compliance - The local regulations over rides all other factors when choosing a region. For workloads bound by data residency laws, it is mandatory to choose a region in that country. 

- Latency - To achieve low latency, the region must be close to the users.

- Cost - For the same service, the cost might differ in different regions. 

- Services and features - Usually larger regions can offer new services and features.  

eu-central-1 (Frankfurt) is preferred over us-west-2 (Oregon)) for these assignments as this is the closest place and the resources need to be set up in a region closest to the users. 















