import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_cdk_py_sqs_sns_01.aws_cdk_py_sqs_sns_01_stack import AwsCdkPySqsSns01Stack


def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkPySqsSns01Stack(app, "aws-cdk-py-sqs-sns-01")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = AwsCdkPySqsSns01Stack(app, "aws-cdk-py-sqs-sns-01")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
