import aws_cdk as cdk
from constructs import Construct
from cdkpipeline.cdkpipeline_lambda_stack import LambdaStack

class PipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = LambdaStack(self, "LambdaStack")