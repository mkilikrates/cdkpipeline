import aws_cdk as cdk
from constructs import Construct
import aws_cdk.aws_ssm as ssm

from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

class CdkpipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        pipeline =  CodePipeline(
            self, 
            "Pipeline", 
            pipeline_name="MyPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub(
                    "mkilikrates/cdkpipeline",
                    "main"
                ),
                commands=[
                    "npm install -g aws-cdk", 
                    "python -m pip install -r requirements.txt", 
                    "cdk synth"
                ]
            )
        )
