'''


import boto3
import json
import logging
import os
import time
import threading
import traceback

from botocore.exceptions import ClientError
from datetime import datetime

log = logging.getLogger()
log.setLevel(logging.INFO)


# Get environment variables
KINESIS_STREAM = os.environ['KINESIS_STREAM']
KINESIS_SHARD_ID = os.environ['KINESIS_SHARD_ID']
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
AWS_REGION = os.environ['AWS_REGION']

# Create boto3 clients
kinesis = boto3.client('kinesis')
dynamodb = boto3.client('dynamodb')
