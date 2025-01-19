import boto3
import json

# Initialize the SageMaker runtime client
sagemaker_runtime = boto3.client('runtime.sagemaker')

# Specify the endpoint name
endpoint_name = 'huggingface-pytorch-inference-2025-01-18-21-54-37-838'

# Prepare the payload for the request (replace with your actual data)
payload = json.dumps({"input": "your input data"})

# Call the SageMaker endpoint
response = sagemaker_runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType='application/json',  # Specify content type (for example, JSON)
    Body=payload  # Send your input data
)

# Process the response
result = json.loads(response['Body'].read().decode())
print(result)
