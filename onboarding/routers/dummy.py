from bson.objectid import ObjectId
import schema
from serializers.userSerializers import userEntity
from Database.mongo import User,Profile
from fastapi import Response, status, Depends, HTTPException,APIRouter,UploadFile,File, Body
from serializers.userSerializers import userEntity, userResponseEntity
from pymongo.collection import ReturnDocument
from fastapi import UploadFile, File, status
import os
from dotenv import load_dotenv
from fastapi.datastructures import UploadFile
from fastapi.exceptions import HTTPException
from fastapi.param_functions import File
from s3_events.s3_utils import S3_SERVICE
from routers.utils import * 
from datetime import datetime
from fastapi import Request, Response, Depends, status, Form
from fastapi.encoders import jsonable_encoder
import os
from dotenv import load_dotenv
from datetime import datetime
import datetime


router = APIRouter()


load_dotenv()


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION")
S3_Bucket = os.environ.get("S3_Bucket")
#S3_Key = os.environ.get("S3_Key")

# Object of S3_SERVICE Class
s3_client = S3_SERVICE(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)


@router.post("/upload", status_code=200, description="***** Upload profile image to S3 *****")
async def upload(fileobject: UploadFile = File(...),name:str=Form(...)):
    filename = fileobject.filename
    current_time = datetime.datetime.now()
    split_file_name = os.path.splitext(filename)   #split the file name into two different path (string + extention)
    file_name_unique = str(current_time.timestamp()).replace('.','')  #for realtime application you must have genertae unique name for the file
    file_extension = split_file_name[1]  #file extention
    data = fileobject.file._file  # Converting tempfile.SpooledTemporaryFile to io.BytesIO
    uploads3 = await s3_client.upload_fileobj(bucket=S3_Bucket, key= file_name_unique +  file_extension, fileobject=data)
    if uploads3:
        s3_url = f"https://{S3_Bucket}.s3.{AWS_REGION}.amazonaws.com/{file_name_unique +  file_extension}"

        data = {"Profile_Photo" : s3_url,'Name': name}

        response = User.insert_one(data)

        return {"status": "success", "image_url": s3_url,"Name":name}  #response added 
    else:
        raise HTTPException(status_code=400, detail="Failed to upload in S3")



@router.post("/users", response_model=schema.about, status_code=status.HTTP_201_CREATED)
async def create_user(Height: float = Body(...),Weight: float = Body(default=None)):
    data = {
        'Height': Height,
        'Weight': Weight
    }
    result = User.insert_one(data)
    return {"status": "success","user":data}



@router.post("/register/v1")
def register(request: Request, height: str = Form(...), weight: str = Form(...)):
    User = jsonable_encoder(schema.about(height=height,weight=weight))
    return User

@router.post("/register/v2")
def register_user(request: Request, name: str = Form(...)):
    User = jsonable_encoder(schema.Username(name=name))
    return User

