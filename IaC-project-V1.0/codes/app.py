#!/usr/bin/env python3
import os
import aws_cdk as cdk

from stacks.SingleStackMvp import SingleStack

app = cdk.App()

SingleStack(app, "singleStack-test")

app.synth() 
