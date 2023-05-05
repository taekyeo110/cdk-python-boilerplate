import aws_cdk as cdk
from aws_cdk import (
    Stack,
    pipelines
)

from .cdk_stage import CdkStage


class CdkPipelineStack(Stack):
    def __init__(self, scope, id, *,
                 description=None,
                 env=None,
                 stackName=None,
                 tags=None,
                 synthesizer=None,
                 terminationProtection=None,
                 analyticsReporting=None):
        super().__init__(scope, id, env=env)

        pipeline = pipelines.CodePipeline(
            self, "Pipeline",
            pipeline_name='pipeline_name (write here)',
            synth=pipelines.ShellStep(
                "Synth",
                # Use a connection created using the AWS console to authenticate to GitHub
                # Other sources are available.
                input=pipelines.CodePipelineSource.git_hub(
                    "Organization name{write here}/repo_name (write here)", "master",
                    # This is optional
                    authentication=cdk.SecretValue.secrets_manager('github-token {write here}')
                ),
                commands=["pip install -r requirements.txt", "npm install -g aws-cdk", "cdk synth"]
            )
        )

        # 'MyApplication' is defined below. Call `addStage` as many times as necessary with any account and region (maybe different from the pipeline's).
        pipeline.add_stage(CdkStage(self, "dev", env=env))
        pipeline.add_stage(CdkStage(self, "live", env=env), pre=[pipelines.ManualApprovalStep("PromoteToProdLive")])
