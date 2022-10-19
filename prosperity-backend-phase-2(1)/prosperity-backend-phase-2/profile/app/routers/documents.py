from fastapi import APIRouter, UploadFile, File
from requests import request
from app import schemas
from app.repository import personal_details, documents
import uuid
import bson
from bson.binary import Binary

from fastapi import APIRouter, Depends
from app.deps import s3_auth
from botocore.client import BaseClient

from botocore.client import BaseClient
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse

from app.deps import s3_auth
from app.repository.documents import upload_file_to_bucket


router = APIRouter(
    prefix="/documents",
    tags=['Documents']
)



@router.get("/")
def get_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()

    return response['Buckets']

@router.post("/aadhar", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets and Mongodb",
             description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
             response_description="Successfully uploaded file to S3 bucket")
def upload_file(id:str, s3: BaseClient = Depends(s3_auth), file_obj: UploadFile = File(...)):


    # Store on mongodb
    documents.doc_upload(id, file_obj, "aadhar")
    upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj.file,
                                       bucket='profile-docs',
                                       folder="aadhar-card",
                                       object_name=file_obj.filename
                                       )

    if upload_obj:
        return JSONResponse(content="Object has been uploaded to bucket successfully",
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")


@router.post("/pan", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets & Mongodb.",
             description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
             response_description="Successfully uploaded file to S3 bucket")
def upload_file(id:str, s3: BaseClient = Depends(s3_auth), file_obj: UploadFile = File(...)):


    # Store on mongodb
    documents.doc_upload(id, file_obj, "pan")

    # Upload to s3
    upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj.file,
                                       bucket='profile-docs',
                                       folder="aadhar-card",
                                       object_name=file_obj.filename,
                                       )

    if upload_obj:
        return JSONResponse(content="Object has been uploaded to bucket successfully",
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")
