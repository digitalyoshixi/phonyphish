import boto3

# Initialize the SageMaker client
sagemaker_client = boto3.client('sagemaker')

# Specify the endpoint name
endpoint_name = 'phishyyyyyy'

# Stop the endpoint (this would need an update operation with a new config, or delete)
response = sagemaker_client.update_endpoint(
    EndpointName=endpoint_name,
    EndpointConfigName='new-endpoint-config-name'  # Provide a new endpoint config if needed
)

print("Stopping endpoint:", response)
