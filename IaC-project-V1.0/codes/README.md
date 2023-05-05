
# Welcome to your CDK Python project V1.0 !

This project makes use of cdk to deploy infrastructure as code in python language. The following are the design considerations for this project

- In Frankfurt region (eu-central), 2 vpcs are launched , one to launch web server and the other to launch admin server. The vpc of web server  uses the cidr range of 10.10.10.0/24 and the vpc of admin server uses cidr in the range of 10.20.20.0/24. For the webServer-vpc, the 2 Azs selected are "eu-central-1a", "eu-central-1b". Each of these Azs consists of one public sunbet .  The public subnets have the cidr range as ['10.10.10.0/25', '10.10.10.128/25'] .The adminServer-vpc has 2 Azs, each Az consisting of one public subnet. The subnets are divided as 10.20.20.0/25 in eu-central-1a and 10.20.20.128/25 in eu-central-1b. 

- The admin server is a windows server in launched in the public subnet of Az, eu-central-1b. 

- The web server is  launched in public subnet of Az, eu-central-1a.

- The administrator logs into the admin server via   RDP protocol and from there into the web server in the public subnet in the other vpc.The outside SSH and RDP connections to the web server are not allowed.

- The VPC peering routes the traffic from between the admin server in the public subnet and the web server in the private subnet.The route table of public subnet associated with the web server is edited to make an entry for the traffic from public subnet of the admin server in the other vpc. Similarly, in the route table of the public subnet of the adminServer-vpc, the cidr block of webServer-vpc is included.

- For logging into the servers, key pair is generated and the private key is stored in the Parameter Store of Systems Manager

- For security at instance level, SGs are implemented and at the sub net level NACLs are implemented.

- The S3 bootstrap bucket is used as the storage solution for user data scripts. It is encrypted by the AWS managed key

- KMS is used to create the encryption keys to encrypt EBS volume of admin server and the web server launched . 


- back up plan - It take the back up of web servers on a daily basis at a specified time and retains it for 7 days.

The entire project has a CDK app with instances of a single stack instantiated in the app.py file .

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
 * `cdk deploy `      deploy all stacks to your default AWS account/region
 * `cdk destroy `      destroys all stacks in your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


