import boto3
from botocore.client import BaseClient

# from app.settings import settings


def s3_auth() -> BaseClient:
    # s3 = boto3.client(service_name='s3', aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
    #                   aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY
    #                   )
    s3 = boto3.client(service_name='s3', aws_access_key_id="AKIATTC6ZSPZV2NAS6F2",
                      aws_secret_access_key="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"
                      )

    return s3
