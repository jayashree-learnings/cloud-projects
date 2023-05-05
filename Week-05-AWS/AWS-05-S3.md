#  AWS Simple Storage Service (S3) 
AWS S3 is an object storage service built to store objects. The storage classes are

S3 standard - Usually used for frequently accessed data. Offers 11 nines of availability and 99.99% durability. It helps in low latency and high throughput. 

S3 standard infrequent access - Slightly cheaper than S3 standard, used for infrequently accessed data which needs to be retrieved fast. Stored in multiple AZs. Has 99.9 % availability.

S3 one zone infrequent access - Has the same functionality as that of S3 standard infrequent access, but stored in only on AZ. Has 99.5 % availability.

S3 glacier instant retrieval - Helps to retrieve the data instantly in milliseconds. Minimum storage is 90 days.

S3 glacier flexible retrieval - Used for slow retrieval of data when compared to S3 glacier instant retrieval. Minimum storage is 90 days.

S3 glacier deep archive - for very long term storage(min- 180 days)

S3 outpost - Used for data which requires local storage.

S3 intelligent tiering - Helps to automatically change the access tiers based on usage.

## Key terminologies
bucket - similar to a directory.

objects - the files stored in a bucket and have version id, meta data, tags, values(content) and key(full path of the object).

bucket policy - Allows to modify the permission tlo access the bucket.

Access Control List (ACL) - read, write , full_control to specific users for an individual bucket or object. 

## Exercise
1. Create new S3 bucket with the following requirements: Region: Frankfurt (eu-central-1)

    ● Upload a cat picture to your bucket.

    ● Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.

2. Create new bucket with the following requirements:Region: Frankfurt eu-central-1)

    ● Upload the four files that make up AWS’ demo website.

    ● Enable static website hosting.

    ● Share the bucket website endpoint with a peer. Make sure they are able to see the website.

### Sources
https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html

https://aws.amazon.com/s3/faqs/?nc=sn&loc=7

https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3

### Overcome challenges
Had to see how to make the url of the uploaded image (i.e. the object) public. Also had to look up on how to host a static website using S3. Understood it when the hands-on-lab was done.

### Results
1) The s3 bucket was created with a global unique name in eu-central(frankfurt) region. The ACL was enabled so that ACL permissions can be edited. Then the 'block all public access' was unchecked so that public has access to the bucket and objects. An image of the cat was uploaded. It was selected and read permission was granted to the public. The url of the uploaded image was tested in a web browser by a colleague and it was verified  that the image was accessible.

enabling ACL 
##### ![AWS-05-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/01-CreateBuckets-ACL-enabled.PNG)

Give public access
##### ![AWS-05-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/02-CreateBucket-BucktAndObjectPublic.PNG)


Object uploaded
##### ![AWS-05-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/03-ObjectUploaded-.PNG)

Editing object ACL
##### ![AWS-05-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/04-ACLOfObjectEdited.PNG)

Image-accessiblity confirmed by a peer
##### ![AWS-05-05](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/05-CatImageAccessible.PNG)


2) An S3 bucket was created and settings was done as above. The files of the static web site were uploaded to the bucket. In the properties tab, static website hosting was enabled. The  files index.html and error.html were specified. All these images were selected at once and made public via ACL (using the actions drop down). The accessibility of the website was tested by a colleague who confirmed that url was accessible using a web browser. 

configuring the settings of static website
##### ![AWS-05-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/StaticWebsite-01.PNG)


accessing the website
##### ![AWS-05-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-05/StaticWebsite-02.PNG)















