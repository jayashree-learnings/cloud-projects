
# Welcome to your CDK Python project V1.1 !

This project makes use of cdk to deploy infrastructure as code in python language. The following are the design considerations for this project

- In Frankfurt region (eu-central), 2 vpcs are launched , one to launch web server and the other to launch admin server. The vpc of web server  uses the cidr range of 10.10.10.0/24 and the vpc of admin server uses cidr in the range of 10.20.20.0/24. For the webServer-vpc, the 2 Azs selected are "eu-central-1a", "eu-central-1b". Each of these Azs consists of one public sunbet and one private subnet with equally divided subnetting.  The public subnets have the cidr range as ['10.10.10.0/26', '10.10.10.64/26'] and private subnet has the cidr range of ['10.10.10.128/26', '10.10.10.192/26']. The adminServer-vpc has 2 Azs, each Az consisting of one public subnet. The subnets are divided as 10.20.20.0/25 in eu-central-1a and 10.20.20.128/25 in eu-central-1b. 

- The admin server is a windows server in launched in the public subnet of Az, eu-central-1b. 

- The web servers are launched in both the Azs by the ASG, the desired number being 2 always.

- The admin server receives SSH and RDP requests and inturn connects  with the web server in the private subnet.The outside SSH and RDP connections to the web servers are not allowed. The admin server also acts a jump host so that the key need not be stored in the parameter store. To install openSSH server in the admin server, the in the NACL the outbound traffic to port 80 and 443 need to be allowed(it was not done in V1) and also, the corresponding inbound traffic

- The VPC peering routes the traffic from between the admin server in the public subnet and the web server in the private subnet.The route table of each private subnet associated with the web server has to edited to make an entry for the traffic from public subnet of the admin server in the other vpc. Similarly, in the route table of the public
subnet of the adminServer-vpc, the cidr block of webServer-vpc is included.

- For logging into the servers, key pair is generated and the private key is stored in the Parameter Store of Systems Manager

- For security at instance level, SGs are implemented and at the sub net level NACLs are implemented.

- A separate S3 bucket is used as the storage solution for user data scripts. It is encrypted by the CMK created by
the user.

- KMS is used to create the encryption keys to encrypt EBS volume of admin server and the web servers launched by ASG. Appropriate roles need to be created with proper permissions. The policy document document mut include the permissions for root principal explicitly since the document gets overwritten and hence, it throws error.

- The ALB is attached to the public subnets of the webServer-vpc. It is configured with a TLS certificate and hence has a listener at port 443. The requests to port 80 are redirected to port443. It has target group at port 80 and also performs health checks at the / (homepage or index.html) of the apache web server at the specified time intervals and declare them as healthy or unhealthy.

- back up plan - It take the back up of web servers on a daily basis at a specified time and retains it for 7 days.

- The ACM is used to store and manage the self signed certificate. A separate python script which makes use of openSSL module was used to create a self signed certificate. It was imported to ACM using boto3. The scrpit checks if a certificate exists and if so, it retrieves the arn ,else it creates a new one and retrieves the arn. 

The entire project has a CDK app with instances of all the 5 stacks (`  KmsStackV2 , AdminServerStackV2 , BackUpStackV2 , S3StackV2 , WebServerStackV2`).These stacks are instantiated in the app.py file and the values are imported and used in other stacks appropriately.

# Prerequisites

The cdk project needs some prerequisites to be installed like aws-cli, npm package , and python.
The detailed information can be found in the aws official documentation here
[click here](https://docs.aws.amazon.com/cdk/v2/guide/work-with.html#work-with-prerequisites)

# Getting started

Once all the prerequisites are met, a new project is created by the following commands. This creates all the required file and folder structure.

```
mkdir my-project
cd my-project
cdk init app --language python
```

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates a virtualenv within this project, stored under the .venv directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`                 list all stacks in the app
 * `cdk synth`              emits the synthesized CloudFormation template
 * `cdk bootstrap`           creates the bootstrap bucket to store CFn template files and necessary roles CDK needs to operate
 * `cdk deploy --all`      deploy all stacks to your default AWS account/region
 * `cdk destroy --all`      destroys all stacks in your default AWS account/region
 * `cdk destroy/deploy stackname`  to destroy/deploy a single stack in your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


