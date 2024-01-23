import boto3
from botocore.exceptions import ClientError

client = boto3.client('ec2')

input_num = input('Enter 1 to create an instance.\nEnter 2 to start an instance.\nEnter 3 to stop an instance.\nEnter 4 to terminate an instance.\n')

if int(input_num) == 1:
    response = client.run_instances(
        ImageId='ami-0a3c3a20c09d6f377',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
    print('Instance created, Instance ID - ' + response['Instances'][0]['InstanceId'])
elif int(input_num) in [2,3,4]:
    instance_id = input('Enter instance ID: ')
    try:
        if int(input_num) == 2:
            response = client.start_instances(InstanceIds=[instance_id])
        if int(input_num) == 3:
            response = client.stop_instances(InstanceIds=[instance_id])
        if int(input_num) == 4:
            response = client.terminate_instances(InstanceIds=[instance_id])
        print(response)
    except ClientError:
        print('Invalid instance ID')
else:
    print('Invalid input')
