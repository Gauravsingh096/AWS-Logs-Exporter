import boto3
import os
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Initialize AWS clients
    logs = boto3.client('logs')
    s3 = boto3.client('s3')
    
    # Time range (last 1 hour)
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    
    # CloudWatch Logs extraction
    log_groups = logs.describe_log_groups()['logGroups']
    
    for group in log_groups:
        log_group_name = group['logGroupName']
        streams = logs.describe_log_streams(logGroupName=log_group_name)['logStreams']
        
        for stream in streams:
            events = logs.get_log_events(
                logGroupName=log_group_name,
                logStreamName=stream['logStreamName'],
                startTime=int(start_time.timestamp() * 1000),
                endTime=int(end_time.timestamp() * 1000)
            )
            
            # Save to S3
            s3_key = f"cloudwatch/{log_group_name}/{stream['logStreamName']}/{end_time.isoformat()}.log"
            s3.put_object(
                Bucket=os.environ['S3_RAW_LOGS_BUCKET'],
                Key=s3_key,
                Body='\n'.join([e['message'] for e in events['events']])
            )
    
    return {"status": "success", "message": "Logs stored in S3"}