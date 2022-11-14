import schema
from Database.mongo import User
from fastapi import  status, HTTPException,APIRouter,UploadFile,File, Body, Request
from fastapi import UploadFile, File, status,Form
import os
from fastapi.datastructures import UploadFile
from fastapi.exceptions import HTTPException
from fastapi.param_functions import File
from s3_events.s3_utils import S3_SERVICE
from routers.utils import * 
from dotenv import load_dotenv
from datetime import datetime,date
import datetime
from schema import Gender
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="../onboarding/templates")
load_dotenv()

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION")
S3_Bucket = os.environ.get("S3_Bucket")
#S3_Key = os.environ.get("S3_Key")

# Object of S3_SERVICE Class
s3_client = S3_SERVICE(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)


## profile picture and name ######################################################

@router.get('/yourself')
async def yourself(request: Request):    
    context = {'request': request}
    return templates.TemplateResponse("yourself.html",context)


@router.post('/yourself')
async def yourself(request: Request):    
    form = await request.form()
    user = ({
        'name': form.get("userName"),
        'img': form.get("img"),
        
    })
    filename = user["img"].filename
    current_time = datetime.datetime.now()
    split_file_name = os.path.splitext(filename)   #split the file name into two different path (string + extention)
    file_name_unique = str(current_time.timestamp()).replace('.','')  #for realtime application you must have genertae unique name for the file
    file_extension = split_file_name[1]  #file extention
    data = user["img"].file._file  # Converting tempfile.SpooledTemporaryFile to io.BytesIO
    uploads3 = await s3_client.upload_fileobj(bucket=S3_Bucket, key= file_name_unique +  file_extension, fileobject=data)
    if uploads3:
        s3_url = f"https://{S3_Bucket}.s3.{AWS_REGION}.amazonaws.com/{file_name_unique +  file_extension}"

        data = {"Profile_Photo" : s3_url,'Name': user["name"]}
        # response = User.insert_one(data)
        context = {'request': request, 'data': data}
        return templates.TemplateResponse("genderDob.html",context)
    else:
        raise HTTPException(status_code=400, detail="Failed to upload in S3")
    


## Height and weight ##############################################################

@router.get('/heightWeight')
async def heightWeight(request: Request):    
    context = {'request': request}          
    return templates.TemplateResponse("heightWeight.html",context)


@router.post("/heightWeight")
async def heightWeight(request: Request,height: float = Form(...), weight: float = Form(...)):
    result = ({
        'Height': height,
        'Weight': weight
    })
    print(result['Height'])
    print(result['Weight'])
    context = {'request': request}       
    return result


## gender and Dob ##################################################################


@router.get('/genderDob')
async def genderDob(request: Request):    
    context = {'request': request}          
    return templates.TemplateResponse("genderDob.html",context)


@router.post("/genderDob")
async def genderDob(request: Request,gender: str = Form(...), dob: str = Form(...)):
    form = await request.form()
    user = ({
        'gender': form.get("gender"),
        'dob': form.get("dob"),
        
    })
    print(user['gender'])
    context = {'request': request, 'user': user}       
    return templates.TemplateResponse("heightWeight.html",context)


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
