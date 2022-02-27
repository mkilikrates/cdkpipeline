#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdkpipeline.cdkpipeline_stack import CdkpipelineStack


app = cdk.App()
region = os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])
account = os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"])

CdkpipelineStack(app, "CdkpipelineStack", env=cdk.Environment(account=account, region=region))

app.synth()
