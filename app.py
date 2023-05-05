#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_project_boiler_plate.cdk_pipeline import CdkPipelineStack


app = cdk.App()
env = cdk.Environment(account="aws account id {write here}", region="ap-northeast-1")

pipeline_stack = CdkPipelineStack(app, "cdk-project-name (write here)", env=env)
cdk.Tags.of(pipeline_stack).add("Service", "service tag {write here}")

app.synth()
