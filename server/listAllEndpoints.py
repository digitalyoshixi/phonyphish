import boto3

# Initialize the SageMaker client
sagemaker_client = boto3.client('sagemaker')

# List all endpoints
response = sagemaker_client.list_endpoints()

# Print the names of all endpoints
for endpoint in response['Endpoints']:
    print(f"Endpoint Name: {endpoint['EndpointName']}, Status: {endpoint['EndpointStatus']}")
