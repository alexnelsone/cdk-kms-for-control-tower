import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_kms_for_control_tower.cdk_kms_for_control_tower_stack import (
    CdkKmsForControlTowerStack,
)


# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_kms_for_control_tower/cdk_kms_for_control_tower_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkKmsForControlTowerStack(app, "cdk-kms-for-control-tower")
    assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
