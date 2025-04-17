import json
import boto3
from datetime import datetime
import logging
logging.basicConfig(filename='/tmp/lambda_logs.txt', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info(f"Recieved Event: {event}")
    logger.info("## EVENT: %s", event)  
    # logger.info("Received event: " + str(event))
    try:
        print("Received event:", json.dumps(event))
        logger.info("Processing started...")
        
        # Your processing logic here
        download_url = "https://example.com/test.csv"
        with open('/tmp/full_logs.txt', 'a') as f:
            f.write(f"{datetime.now()} - Processed: {event}\n")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Success", 
                "input_event": event })
        }
        
        # return {
        #     "statusCode": 200,
        #     "body": json.dumps({
        #         "message": "Success",
        #         "download_url": download_url
        #     })
        # }
    #     return {
    #     "statusCode": 200,
    #     "body": json.dumps({
    #         "message": "Logs stored in /tmp/full_logs.txt",
    #         "download_command": "aws lambda invoke --function-name ConvertLogsToCSV --payload '{\"action\":\"download_logs\"}' output.json"
    #     })
    # }
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
