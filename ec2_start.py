import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-south-1')

    # List of specific instance IDs to start
    allowed_instances = ['i-0a8c8047505c17a04', 'i-011a3bcc0830bdae2', 'i-099545fc8dc436dd4']

    # Get all stopped instances that are in the allowed list
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

    instances_to_start = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            if instance_id in allowed_instances:
                instances_to_start.append(instance_id)

    if instances_to_start:
        ec2.start_instances(InstanceIds=instances_to_start)
        print(f"Starting instances: {instances_to_start}")
        return {
            'statusCode': 200,
            'body': f'Started instances: {instances_to_start}'
        }
    else:
        print("No matching stopped instances found in the allowed list.")
        return {
            'statusCode': 400,
            'body': 'No matching stopped instances found in the allowed list.'
        }
