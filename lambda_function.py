import boto3
import json
import urllib
import random
import time
from datetime import datetime
import logging
import os
from base64 import b64decode

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    reqBody = event['body']
    params = urllib.parse.parse_qs(reqBody)
    token = params['token'][0]
    ENCRYPTED_TOKEN = os.environ['SLACK_TOKEN']
    DECRYPTED_TOKEN = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED_TOKEN))['Plaintext'].decode()
    if token != DECRYPTED_TOKEN:
        logger.error("Request token (%s) does not match exptected", token)
        raise Exception("Invalid request token")

    commandText = params['text'][0]
    channelId = params['channel_id'][0]
    processId = "id-" + str(random.randint(1000000000,9999999999) - 10)
    startUnixTime = round(time.time())
    print(startUnixTime)
    awsLambda = boto3.client('lambda')
    response = awsLambda.invoke(
        FunctionName='operateEc2',
        InvocationType='Event',
        Payload= json.dumps({
            "text": commandText,
            "channel_id": channelId,
            "process_id": processId,
            "start_unix_time": startUnixTime
        })
    )

    return {
        "text": "実行中です...\nID:" + processId,
        "response_type": "in_channel"
    }