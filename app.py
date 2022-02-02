#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.vpc_stack import VPCStack
from stacks.security_stack import SecurityStack
from stacks.bastion_stack import BastionStack
from stacks.kms_stack import KMSStack

app = cdk.App()

vpc_stack = VPCStack(app, 'vpc')
security_stack = SecurityStack(app, 'security-stack', vpc=vpc_stack.vpc)
bastion_stack = BastionStack(app, 'bastion', vpc=vpc_stack.vpc,sg=security_stack.bastion_sg)
kms_stack = KMSStack(app, 'kms')

app.synth()
