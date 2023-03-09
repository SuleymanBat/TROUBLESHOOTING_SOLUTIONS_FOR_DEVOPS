import boto3
import re
from datetime import datetime

def lambda_handler(event, context):


    TERMINATION_AGE = 0
    
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    
    # Get a list of stopped instances
    instances = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
    
            # StateTransitionReason might be like "i-xxxxxxxx User initiated (2016-05-23 17:27:19 GMT)"
            reason = instance['StateTransitionReason']
            date_string = re.search('User initiated \(([\d-]*)', reason).group(1)
            if len(date_string) == 10:
                date = datetime.strptime(date_string, '%Y-%m-%d')
    
                # Terminate if older than TERMINATION_AGE
                if (datetime.today() - date).days + 1 > TERMINATION_AGE:
                    ec2_client.terminate_instances(InstanceIds=[instance['InstanceId']])
            