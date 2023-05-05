import aws_cdk as core
import aws_cdk.assertions as assertions
from cdk_project_boiler_plate.cdk_stack import CdkStack


def test_sqs_queue_created():
    app = core.App()
    stack = CdkStack(app, "cdk stack name (write here)")
    # template = assertions.Template.from_stack(stack)
    #
    # template.has_resource_properties("AWS::SQS::Queue", {
    #     "VisibilityTimeout": 300
    # })
