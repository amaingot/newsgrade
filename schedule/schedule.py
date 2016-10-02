import time
import boto.sqs
from boto.sqs.message import Message
from datetime import datetime
import settings


sqs = boto.sqs.connect_to_region(
                settings.sqs_region,
                aws_access_key_id=settings.aws_user_key,
                aws_secret_access_key=settings.aws_user_secret)
queue = sqs.get_queue(settings.sqs_name)



while (true):
    # Query for news sources


    # For each news source, queue 