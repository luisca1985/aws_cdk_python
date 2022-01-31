#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.vpc_stack import VPCStack

app = cdk.App()

vpc_stack = VPCStack(app, 'vpc')

app.synth()