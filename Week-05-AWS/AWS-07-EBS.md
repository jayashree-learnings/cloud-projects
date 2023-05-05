#  AWS EBS
AWS Elastic Block Store(EBS) is a storage service allowing the instance to persist the data even after termination. An EBS volume in an AZ can be attached to an EC2 in the same AZ.  The two main categories are SSD and HDD. 
SSD based volumes are divided into 5 types- io2,io2 block express, io1, gp3, gp2.

io2 - Mainly used for business critical platforms where there is no room for latency

io2 block express -  Highest performance block storage. 

io1 - Built for both IOPS-sensitive and throughput-sensitive transactional workloads.

gp3 - Latest general purpose SSD volume that balances the price and  performance for a wide variety of transactional workloads.

gp2 - Default EBS volume of EC2 instances.
 
HDD based volumes are st1 and sc1. 

st1 - Low cost HDD volume for frequently accessed throughput-intensive workloads.

sc1 - Lowest cost HDD volume meant for less frequently accessed workloads.


## Key terminologies

EBS volume - An instance of an EBS.

Snapshot - created as back up from which new volumes can be created. 

Throughput - Amount of data that flows through a data path in a given time.(similar to counting characters per second)

IOPS - Input-Output operations per second. measures the transactions processed per second.(similar to counting words per second) 

latency - time take to process data request or transaction.

root volume - the default volume created at the root level when the ec2 instance is lunched. It gets deleted when instance is terminated.

non-root volume - the volume the user creates. It has to be deleted explicitly after terminating the instance.

## Exercise
1. Navigate to the EC2 menu. Create a t2.micro Amazon Linux 2 machine with all the default settings.Create a new EBS volume with the requirements:
    - Volume type: General Purpose SSD (gp3)
    - Size: 1 GiB
    - Availability Zone: same as your EC2
    - Wait for its state to be available.

2. Attach your new EBS volume to your EC2 instance. Connect to your EC2 instance using SSH. Mount the EBS volume on your instance.
Create a text file and write it to the mounted EBS volume.

3. Create a snapshot of your EBS volume. Remove the text file from your original EBS volume. Create a new volume using your snapshot.
Detach your original EBS volume. Attach the new volume to your EC2 and mount it. Find your text file on the new EBS volume.

### Sources
https://aws.amazon.com/ebs/

https://aws.amazon.com/ebs/faqs/

https://www.youtube.com/watch?v=vjyQwYml3Lg&list=PL_PQZlQoXVJFi-RIdL0MHG9c-qaZwFG8d&index=33


### Overcome challenges
Had to see how to mount a device to a mounting point., how to create a new ebs volume, attach it to an ec2 instance, detach it. Also had to look up on how to create a snap shot of an EBS volume and create a volume out of it. Understood it by doing the practical exercise.

### Results
1) In the first exercise, an ec2 instance was launched and a new EBS volume in the same AZ was created.

launching ec2
##### ![AWS-07-01](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/01-ec2launch-sameSG.PNG)


created a new volume in same AZ
##### ![AWS-07-02](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/02-NewVolumeinSameAZ.PNG)

2) The newly created EBS volume was attached to the ec2 instance. After logging into the system via SSH, the attached EBS volume was mounted by using a newly created directory in /mnt and using it as the mount point. A text file was created in the same directory and its contents were displayed.

Attaching volume to ec2
##### ![AWS-07-03](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/03-AttachEBStoec2.PNG)

verifying volume is attached
##### ![AWS-07-04](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/04-VerifyAttachedVolume.PNG)

Formatting and mounting the volume
##### ![AWS-07-05a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/05a-FormatAndMount.PNG)


creating file in the mount point
##### ![AWS-07-05b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/05b-CreateFileinTheMountPoint.PNG)

3) A snapshot of the EBS volume was created. After that the text file was deleted from the folder. The EBS volume was un mounted, detached and deleted. A new volume was created from the snapshot. It was attached to the ec2, mounted using a different directory in /mnt folder. The text file was available in this new directory as well and its contents could be displayed.  

Snap shot created
##### ![AWS-07-06](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/06-SnapShotCreated.PNG)

Removing file and unmounting device
##### ![AWS-07-07a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/07a-removeFileUnmountDevice.PNG)

detached the volume
##### ![AWS-07-07b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/07b-DetachedTestVolume.PNG)

create volume from snap shot
##### ![AWS-07-08a](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/08a-CreateVolFromSnapShot.PNG)

new volume attached to ec2
##### ![AWS-07-08b](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/08b-VolumeAttachedtoEC2.PNG)

verify that it is attached
##### ![AWS-07-08c](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/08c-verifyNewVolumeAttached.PNG)


file visible in the new volume
##### ![AWS-07-08d](https://github.com/Techgrounds-Cloud-9/cloud-9-jsm-1985/blob/main/00_includes/Week-05/AWS-07/08d-FileAvailableinNewVolume.PNG)








