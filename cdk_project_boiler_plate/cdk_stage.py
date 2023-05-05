import imp
from aws_cdk import (
    Stage,
    Tags
)

from .cdk_stack import CdkStack


class CdkStage(Stage):
    def __init__(self, scope, id, *, env=None, outdir=None):
        super().__init__(scope, id, env=env, outdir=outdir)

        cdk_stack = CdkStack(self, "CdkStack (write here)", stage=id)
        Tags.of(cdk_stack).add("Service", "tag_name {write here}")
