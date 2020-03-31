import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    
    region = 'ap-northeast-1'
    instances = event['Instances']
    try:
        ec2 = boto3.client('ec2', region_name=region)
        ec2.start_instances(InstanceIds=instances)
    except Exception as e:
        logger.error(str(e))
        return {
            "statusCode": 500,
            "message": 'An error has occured at automatically starting ec2 instances'
        }
    else:
        logger.info("Succeeded to start instances... {0}".format(', '.join(instances)))
        return {
            "statusCode": 200,
            "message": 'Finished automatically starting ec2 instances'
        }