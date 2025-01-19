import boto3

# Initialize the SageMaker client
sagemaker_client = boto3.client('sagemaker')

# Specify the endpoint name (replace with your actual endpoint name)
endpoint_name = 'huggingface-pytorch-inference-2025-01-18-21-54-37-838'

# Get details of the endpoint
response = sagemaker_client.describe_endpoint(EndpointName=endpoint_name)

# Print details about the endpoint
print(response)
