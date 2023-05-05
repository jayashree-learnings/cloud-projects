
from constructs import Construct
import aws_cdk as cdk
import json
from aws_cdk import (Stack, 
                     aws_iam as iam, 
                     aws_kms as kms, 
)
                     



class KmsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        print("this is KMS stack")
                
        # KMS key for encrypting EBS device of admin Server        
        adminServer_EBSVol_KMSKey = kms.Key(
                self, 
                "adminServerEBSVolKey", 
                alias = "adminServerEBSEncryptionKey",
                removal_policy  = cdk.RemovalPolicy.DESTROY, 
                enable_key_rotation= True
        )

        # making it an attribute of this class so as to use it in admin server stack
        self.adminServer_ebsVol_kmsKey = adminServer_EBSVol_KMSKey

        # creating a role for ASG                  
        role_ASG = iam.Role.from_role_arn(self,"imported role","arn:aws:iam::762044230457:role/aws-service-role/autoscaling.amazonaws.com/AWSServiceRoleForAutoScaling")
                
        # define policy statements for root principal and ASG-role
        statement1 = iam.PolicyStatement(
                principals = [iam.AccountRootPrincipal()],
                actions = ["kms:*"],
                resources=["*"],
                effect=iam.Effect.ALLOW
        )
        statement2 = iam.PolicyStatement(
                principals = [role_ASG],
                actions = ["kms:Encrypt","kms:Decrypt", "kms:ReEncrypt*","kms:GenerateDataKey*","kms:DescribeKey"],
                resources=["*"],
                effect=iam.Effect.ALLOW
        )  

        statement3 = iam.PolicyStatement(
                principals = [role_ASG],
                actions = ["kms:ListGrants", "kms:CreateGrant", "kms:RevokeGrant"],
                resources=["*"],
                effect=iam.Effect.ALLOW
        )  
        statement3.add_condition("Bool", {"kms:GrantIsForAWSResource": True}) 
          
        # define key policy for ASG
        keyPolicy_ASG = iam.PolicyDocument(
               statements = [ statement1, statement2, statement3]
        )

        # define Web Server KMS key for encryption       
        webServer_EBSVol_KMSKey = kms.Key(
                self,
                "webServerEBSVolKey", 
                policy=keyPolicy_ASG,
                alias = "webServerEBSEncryptionKey",
                removal_policy  = cdk.RemovalPolicy.DESTROY, 
                enable_key_rotation= True                               
        )  

        # making it an attribute of this class so as to use it in server stack
        self.webServer_ebsVol_kmsKey = webServer_EBSVol_KMSKey

        # define Web Server KMS key for encryption           
        server_backUpVault_KMSKey = kms.Key(
                self, 
                "ServerVaultKey", 
                alias = "ServerBackUpVaultEncryptionKey",
                removal_policy  = cdk.RemovalPolicy.DESTROY, 
                enable_key_rotation= True
        )

        # making it an attribute of this class so as to use it in back up stack
        self.webServer_vault_kmsKey = server_backUpVault_KMSKey

        # define  KMS key for s3 encryption           
        s3_bkt_KMSKey = kms.Key(
                self, 
                "S3BucketKey", 
                alias = "S3EncryptionKey",
                removal_policy  = cdk.RemovalPolicy.DESTROY, 
                enable_key_rotation= True
        )

        # making it an attribute of this class so as to use it in webSever stack
        self.s3_kmsKey = s3_bkt_KMSKey

       











         

                         
                                                 
                                           
        
        
        
                               




                                                                                         
                                                 
                                                 
                                           
        
        
        
                               


