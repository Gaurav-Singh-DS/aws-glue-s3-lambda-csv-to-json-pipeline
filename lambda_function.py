import json
import boto3

glue_access = boto3.client('glue')

def lambda_handler(event, context):
    glue_access.start_job_run(JobName = 'glue_lambda')
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Job Started sucessfully')
    }
