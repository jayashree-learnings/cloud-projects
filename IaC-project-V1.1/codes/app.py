#!/usr/bin/env python3

import aws_cdk as cdk

################ Single stack execution ###########

# from stacks.SingleStackVersion2 import NewProjectStack
# app = cdk.App()
# NewProjectStack(app, "v2")
# app.synth()



# multi stack execution
from stacks.kmsStack import KmsStack
from stacks.webServerStack import WebServerStack
from stacks.adminServerStack import AdminServerStack
from stacks.backUpStack import BackUpStack
from stacks.s3Stack import S3BucketStack


# instantiate the imported classes
app = cdk.App()

kms_stack = KmsStack(app,"KmsStackV2")

adminServer_stack = AdminServerStack(app, "AdminServerStackV2", adminServer_ebsVolKey= kms_stack.adminServer_ebsVol_kmsKey )

s3_stack = S3BucketStack(app,"S3StackV2",bkt_key = kms_stack.s3_kmsKey)

webServer_stack = WebServerStack(app,"WebServerStackV2",
    webServer_ebsVolKey = kms_stack.webServer_ebsVol_kmsKey,
    admin_server_vpc = adminServer_stack.adminServer_vpc,
    s3_userData_bkt = s3_stack.userData_bkt,
    webServer_key = adminServer_stack.server_keyPair
)

backup_stack = BackUpStack(app,"BackUpStackV2", webServer_vaultKey= kms_stack.webServer_vault_kmsKey)

app.synth()


