
from certs.certCreateImport import cert_arn
from constructs import Construct
import aws_cdk as cdk
import json
from aws_cdk import (Stack, 
                     aws_ec2 as ec2,
                    aws_iam as iam, 
                    aws_kms as kms, 
                    aws_backup as backup,
                    aws_events as events, 
                    aws_iam as iam,                     
                     Tags,
                     Duration )
                     

class BackUpStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, webServer_vaultKey:kms.Key, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        print("this is backUpStack")
                    
        # back up policy  for web server        
        server_backUpVault = backup.BackupVault(
            self, 
            "ServerBackUpVault" , 
            backup_vault_name = "BackUpVaultServer",
            encryption_key = webServer_vaultKey,
            removal_policy = cdk.RemovalPolicy.DESTROY
        )

        webServer_backUpPlan = backup.BackupPlan(self, "BackUpPlanWebServer", backup_plan_name = "WebServerBackUpPlan")
        webServer_backUpPlan.add_selection(
               "WebServer-Selection", 
                resources = [backup.BackupResource.from_tag(key= "name", value = "AutoscalingGroupOfWebServer")]
                                                         
        )                                                                                                  
                                                    
        # Web Server backUp plan rule creating daily backups
        webServer_backUpPlan.add_rule(
            backup.BackupPlanRule(
                backup_vault= server_backUpVault,
                rule_name= "WebServerBackUpRule"  ,
                delete_after = Duration.days(7),
                schedule_expression = events.Schedule.cron(
                    week_day = '*',
                    hour = '5',
                    minute = '0'))
        )

       







         

                         
                                                 
                                           
        
        
        
                               


