import boto3

client = boto3.client('ec2')

# Insert your Instance ID here
my_instance = 'your instance id here'

# Stop the instance
def lambda_handler(event, context):
    client.stop_instances(InstanceIds=[my_instance])
    waiter=client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[my_instance])
    # Change the instance type
    client.modify_instance_attribute(InstanceId=my_instance, Attribute='instanceType', Value='m4.large')
    # Start the instance
    client.start_instances(InstanceIds=[my_instance])
    return {}
