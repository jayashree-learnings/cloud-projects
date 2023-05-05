from certs.certCreateImport import cert_arn
from constructs import Construct
import aws_cdk as cdk
import json
from aws_cdk import (Stack, 
                     aws_ec2 as ec2,
                     aws_kms as kms, 
                     aws_iam as iam,
                     aws_s3 as s3, 
                     aws_s3_deployment as s3deploy,
                     Tags,
                     Duration )
  
class S3BucketStack(Stack):
    def __init__(self, scope: Construct, construct_id: str,  bkt_key:kms.Key, **kwargs) -> None:
        super().__init__(scope,construct_id, **kwargs)
        print("this is s3 stack")
        
        userData_path = "./UserData"
        
        #  defining the bucket
        bkt_userData = s3.Bucket(
            self, 
            "BktToStoreUserData",
            bucket_name = "bkt-storing-bootstrap-script",
            block_public_access = s3.BlockPublicAccess.BLOCK_ALL, 
            bucket_key_enabled = True ,
            encryption_key = bkt_key,
            removal_policy = cdk.RemovalPolicy.DESTROY ,
            auto_delete_objects = True                                                   
        )

        # uploading the user data to the s3 bucket
        userData_deployment = s3deploy.BucketDeployment(
            self, 
            "ToDeployUserData",
            destination_bucket = bkt_userData,
            sources = [s3deploy.Source.asset(userData_path)]                                                                                    
        )

        # making it an attribute of this class so as to access it in web server stack 
        self.userData_bkt = bkt_userData

        
                                                 
                                           
        
        
        
                               


                                                                 
                                                 
                                                 
                                           
        
        
        
                               


