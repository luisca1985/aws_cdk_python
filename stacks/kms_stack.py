from ast import alias
import os
import aws_cdk as cdk
from aws_cdk import (
    aws_kms as kms,
    aws_ssm as ssm
    )
from constructs import Construct


class KMSStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        prj_name = self.node.try_get_context('project_name')
        env_name = self.node.try_get_context('env')

        self.kms_rds = kms.Key(
            self, 'rdskey',
            description=f'{ prj_name }-key-rds',
            enable_key_rotation=True,
        )

        self.kms_rds.add_alias(
            alias_name=os.path.join('alias', f'{ prj_name }-key-rds')
        )

        # Create SSM parameter
        ssm.StringParameter(
            self, 'rdskey-param',
            string_value=self.kms_rds.key_id,
            parameter_name=os.path.join('/', env_name,'rds-kms-key')
        )
