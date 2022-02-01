from email.utils import encode_rfc2231
import aws_cdk as cdk
from aws_cdk import (
    aws_ec2 as ec2
)
from constructs import Construct


class BastionStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, sg: ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bastion_host = ec2.Instance(
            self, 'bastion-host',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.AmazonLinuxImage(
                edition=ec2.AmazonLinuxEdition.STANDARD,
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                virtualization=ec2.AmazonLinuxVirt.HVM,
                storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            ),
            vpc=vpc,
            key_name='devops',
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=sg
        )
