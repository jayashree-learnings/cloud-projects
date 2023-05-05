#  AWS Pricing

The 3 principles of AWS pricing are compute, storage and outbound data transfer. For most of the cases, there is no charge for inbound data transfer or for data transfer between services within the region.

## Key terminologies 

TCO - Total Cost of Ownership - It is the total sum of of all the costs involved in the purchase, operation and maintenance of a given asset during its life time. 


## Exercise
1) The four advantages of the AWS pricing model.
2) AWS free tier for:
- S3
- EC2
-  Always free services
3) Understand the differences between CapEx and OpEx

### Sources

https://docs.aws.amazon.com/pdfs/whitepapers/latest/how-aws-pricing-works/how-aws-pricing-works.pdf

https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all

https://acloudguru.com/forums/aws-certified-cloud-practitioner/benefit-from-massive-economies-of-scale-can-someone-explain-this-to-me-in-more-detail-please

https://www.cloudzero.com/blog/capex-vs-opex

https://www.geeksforgeeks.org/capex-vs-opex-in-cloud-computing/

https://www.cloudzero.com/blog/cloud-tco

### Overcome challenges

Had to see the pricing model of AWS, what are its advantages and what are the different expenditures involved. 


### Results
1) The advantages of AWS pricing model are 

pay-as-you-go - For most of the cloud services, aws offers this option. you have to pay for the services as per consumption without requiring long term contracts or complex licensing. Once you stop using them , there are no additional costs or termination fees.

save when you commit - Savings plans help to save on services more than the on-demand plan for a commitment period of 1 to 3 years. It offers lower price on AWS compute and AWS machine learning. 

pay less by using more - For services like S3 and data transfer OUT from EC2, pricing decrease with the increase in usage. 

benefits from massive economies of scale - As the customers increase, the infrastructure needs to increase, but the cost will now be spread across many customers. the infra structure becomes cheaper and new customers can benefit from the cheap prices.

2) AWS offers free tier for the following services as follows

- s3 -  5 GB of standard storage. 20,000 get requests and 2000 put requests.

- ec2 - 750 hrs/month (Linux, RHEL, Windows t2.micro/t3.micro) depending on the region. 

- always free services - The following services are free

- amazon dynamo DB - 200 million requests per month, 25 GB storage

- Amazon S3 Glacier - Can retrieve 10 GB of data per month for free(std. retrieval using Glacier API)

- Amazon lambda - 1 million free requests per month upto 3.2 million seconds of compute time per month.

3) CapEx - The cost a business incurs to acquire assets that will provide benefits beyond the current year.

OpEx - It is the amount the organization has to spend to run their daily activities.

The differences are

1) In CapEx, the payments are made upfront. In OpEx, it is made on a pay-as-you-go pricing.

2) CapEx requires huge investments that tie up cah in long term investments. In OpEx, the amount is relatively small. 

3) In CapeE, mostly over buying is done to meet future demands. In OpEx, cash flow can be freed to invest in other areas.

4) Tax deduction is over time in CapEx while its in the same year in OpEx.

5) Return from the investment is gradual over the life cycle of asset in CapEx, while in OpEx it is in short billing periods.

6) Maintenance is significant in CapEx, while for OpEx its less.

7) For CapEx the value over the time lowers, in OpEx there is no much change. 













