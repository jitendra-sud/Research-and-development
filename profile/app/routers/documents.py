from fastapi import APIRouter, UploadFile, File, Request
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

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    prefix="",
    tags=['Documents']
)



@router.get("/")
def get_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()
    return response['Buckets']

@router.get("/profileDocuments",response_model = schemas.ShowPersonalDetails)
def show(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileDocuments.html",context)

@router.post("/profileDocuments", status_code=status.HTTP_201_CREATED, response_model = schemas.ShowPersonalDetails, summary="Upload files to AWS S3 Buckets and Mongodb",
             description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
             response_description="Successfully uploaded file to S3 bucket" )
async def create(request: Request , s3: BaseClient = Depends(s3_auth) , addhar: UploadFile = File(...), pan: UploadFile = File(...)):
    # form = await request.form()
    id = "636cab4bb55753f1580a2697"
    file_obj_addhar = addhar
    file_obj_pan = pan

    user = ({
        'addhar': file_obj_addhar,
        'pan': file_obj_pan
    })

    
    ##Addhar
    file_obj_addhar.filename = str(uuid.uuid4())+ "." + file_obj_addhar.filename.split(".")[1]
    url = f"https://profile-docs.s3.amazonaws.com/{file_obj_addhar.filename}"

    ##Pan
    file_obj_pan.filename = str(uuid.uuid4())+ "." + file_obj_pan.filename.split(".")[1]
    url = f"https://profile-docs.s3.amazonaws.com/{file_obj_pan.filename}"

    # Store on mongodb ADDHAR
    documents.doc_upload(id, file_obj_addhar, "aadhar", url)

    upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj_addhar.file,
                                       bucket='profile-docs',
                                       folder="aadhar-card",
                                       object_name=file_obj_addhar.filename
                                       )

     # Store on mongodb PAN
    documents.doc_upload(id, file_obj_pan, "pan",url)

    # Upload to s3
    upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj_pan.file,
                                       bucket='profile-docs',
                                       folder="aadhar-card",
                                       object_name=file_obj_pan.filename,
                                       )

    if upload_obj:
        context = {'request': request, 'user': user}
        return templates.TemplateResponse("profiles/profileCoverage.html",context)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")


    print(user["addhar"])
    context = {'request':request, 'user': user}    
    return templates.TemplateResponse("profiles/profileDocuments.html",context)


# @router.post("/aadhar", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets and Mongodb",
#              description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
#              response_description="Successfully uploaded file to S3 bucket")
# def upload_aadhar(id:str, s3: BaseClient = Depends(s3_auth), file_obj: UploadFile = File(...)):    
#     print(file_obj.filename)
#     file_obj.filename = str(uuid.uuid4())+ "." + file_obj.filename.split(".")[1]
    
#     url = f"https://profile-docs.s3.amazonaws.com/{file_obj.filename}"

#     # Store on mongodb
#     documents.doc_upload(id, file_obj, "aadhar", url)

#     upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj.file,
#                                        bucket='profile-docs',
#                                        folder="aadhar-card",
#                                        object_name=file_obj.filename
#                                        )


#     if upload_obj:
#         return JSONResponse(content="Object has been uploaded to bucket successfully",
#                             status_code=status.HTTP_201_CREATED)
#     else:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail="File could not be uploaded")


# @router.post("/pan", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets & Mongodb.",
#              description="Upload a valid file to AWS S3 bucket", name="POST files to AWS S3",
#              response_description="Successfully uploaded file to S3 bucket")
# def upload_file(id:str, s3: BaseClient = Depends(s3_auth), file_obj: UploadFile = File(...)):


#     print(file_obj.filename)
#     file_obj.filename = str(uuid.uuid4())+ "." + file_obj.filename.split(".")[1]

#     url = f"https://profile-docs.s3.amazonaws.com/{file_obj.filename}"

#     # Store on mongodb
#     documents.doc_upload(id, file_obj, "pan",url)

#     # Upload to s3
#     upload_obj = upload_file_to_bucket(s3_client=s3, file_obj=file_obj.file,
#                                        bucket='profile-docs',
#                                        folder="aadhar-card",
#                                        object_name=file_obj.filename,
#                                        )

#     if upload_obj:
#         return JSONResponse(content="Object has been uploaded to bucket successfully",
#                             status_code=status.HTTP_201_CREATED)
#     else:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail="File could not be uploaded")
