import boto3
from dotenv import load_dotenv
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
# List all endpoints
response = sagemaker_client.list_endpoints()

# Print the names of all endpoints
for endpoint in response['Endpoints']:
    print(f"Endpoint Name: {endpoint['EndpointName']}, Status: {endpoint['EndpointStatus']}")
