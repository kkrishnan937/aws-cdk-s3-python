#!/usr/bin/env python3

import aws_cdk as cdk

from cdkdemo.cdkdemo_stack import CdkdemoStack


app = cdk.App()
CdkdemoStack(app, "CdkdemoStack")

app.synth()
