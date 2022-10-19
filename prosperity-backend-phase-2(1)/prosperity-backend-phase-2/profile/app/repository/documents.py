
from urllib import request
from fastapi import HTTPException, status, UploadFile, File
from app import schemas
from app.db import collection_users, collection_aadhar,collection_pan
import uuid
import bson
from bson.binary import Binary
from bson import ObjectId
import logging

from botocore.exceptions import ClientError
from enum import Enum

from botocore.client import BaseClient
from fastapi import Depends

from app.deps import s3_auth


def doc_upload(id, file, doc):
    encoded = Binary(file.file.read())
    user = collection_users.find_one({"_id": ObjectId(id)})
    user[doc]=encoded
    collection_users.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": user
    })
    return {"Successfully uploaded."}

def upload_file_to_bucket(s3_client, file_obj, bucket, folder, object_name=None):
    """Upload a file to an S3 bucket

    :param file_obj: File to upload
    :param bucket: Bucket to upload to
    :param folder: Folder to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name

    filename = str(uuid.uuid4())
    
    if object_name is None:
        object_name = file_obj

    suffix = object_name.split(".")[1]

    # Upload the file
    try:
        response = s3_client.upload_fileobj(file_obj, bucket, f"{filename}.{suffix}")
        location = s3_client.get_bucket_location(Bucket=bucket)['LocationConstraint']

        url = f"https://profile-docs.s3.amazonaws.com/{filename}.{suffix}"

        print(url)
    except ClientError as e:
        logging.error(e)
        return False

    return True



def get_list_of_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()
    buckets = {}

    for buckets in response['Buckets']:
        buckets[response['Name']] = response['Name']

    BucketName = Enum('BucketName', buckets)

    return BucketName

