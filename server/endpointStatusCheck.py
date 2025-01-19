from dotenv import load_dotenv
import boto3
import os

load_dotenv()

# Now you can access AWS credentials via environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_DEFAULT_REGION")
# Initialize the SageMaker client
sagemaker_client = boto3.client('sagemaker',
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )

# Specify the endpoint name (replace with your actual endpoint name)
endpoint_name = 'huggingface-pytorch-inference-2025-01-18-21-54-37-838'

# Get details of the endpoint
response = sagemaker_client.describe_endpoint(EndpointName=endpoint_name)

# Print details about the endpoint
print(response)
