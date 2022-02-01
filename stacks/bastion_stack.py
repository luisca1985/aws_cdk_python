import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ssm as ssm
)
from constructs import Construct

class BastionStack(cdk.Stack):
    def __init__(self, scope: Construct,id: str, vpc: ec2.Vpc, sg: ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope,id,**kwargs)