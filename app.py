#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_py_sqs_sns_01.aws_cdk_py_sqs_sns_01_stack import AwsCdkPySqsSns01Stack


app = cdk.App()
AwsCdkPySqsSns01Stack(app, "aws-cdk-py-sqs-sns-01")

app.synth()
