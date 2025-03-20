import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')

    # List of specific instance IDs to stop
    specific_instances = ['i-0a8c8047505c17a04', 'i-011a3bcc0830bdae2', 'i-099545fc8dc436dd4']

    # Get all running instances
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    instances_to_stop = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            if instance_id in specific_instances:
                instances_to_stop.append(instance_id)

    if instances_to_stop:
        ec2.stop_instances(InstanceIds=instances_to_stop)
        print(f"Stopping instances: {instances_to_stop}")
        return {
            'statusCode': 200,
            'body': f'Stopped instances: {instances_to_stop}'
        }
    else:
        print("No matching running instances found to stop.")
        return {
            'statusCode': 400,
            'body': 'No matching running instances found to stop.'
        }
