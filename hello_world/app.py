#!/usr/bin/env python3

import aws_cdk as cdk

from hello_world.hello_world_stack import HelloWorldStack


app = cdk.App()
HelloWorldStack(app, "hello-world")

app.synth()
