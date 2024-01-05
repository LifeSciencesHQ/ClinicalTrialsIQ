import aws_cdk as core
import aws_cdk.assertions as assertions

from ciq_core.ciq_core_stack import CiqCoreStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ciq_core/ciq_core_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CiqCoreStack(app, "ciq-core")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
