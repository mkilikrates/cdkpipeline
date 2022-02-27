from ast import Lambda
import aws_cdk as cdk
from constructs import Construct
from aws_cdk.aws_lambda import Function, InlineCode, Runtime
import aws_cdk.aws_apigateway as apigateway

class LambdaStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The Lambda function that contains the functionality
        handler = Function(self, "LambdaFunction", 
            runtime=Runtime.NODEJS_12_X,
            handler="index.handler",
            code=InlineCode("exports.handler = _ => 'Hello, CDK';")
        )

        # An API Gateway to make the Lambda web-accessible
        gw = apigateway.LambdaRestApi(
            self,
            'Gateway',
            description='Endpoint for a simple Lambda-powered web service',
            handler=handler
        )
        self.urlOutput = cdk.CfnOutput(
            self,
            'Url',
            value=gw.url
        )


