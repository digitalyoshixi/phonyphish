import boto3
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Now you can access AWS credentials via environment variables
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_DEFAULT_REGION")

# Initialize the SageMaker runtime client
sagemaker_runtime = boto3.client(
    'sagemaker-runtime',  # Corrected client name
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
# Specify the endpoint name
endpoint_name = 'huggingface-pytorch-inference-2025-01-18-21-54-37-838'

# Prepare the payload for the request (replace with your actual data)
payload = json.dumps({"inputs": "test test test"})

try:
    # Call the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',  # Specify content type (for example, JSON)
        Body=payload  # Send your input data
    )
    # Process the response
    result = json.loads(response['Body'].read().decode())
    print(result)
except boto3.exceptions.Boto3Error as e:
    print(f"An error occurred: {e}")
