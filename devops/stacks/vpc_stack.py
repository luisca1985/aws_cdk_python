import aws_cdk as core
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ssm as ssm,
)
from constructs import (
    Construct,
    # Node
)


class VPCStack(core.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        prj_name = self.node.try_get_context('project_name')
        env_name = self.node.try_get_context('env')
