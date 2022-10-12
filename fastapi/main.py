from ast import Num, Str
from multiprocessing import context
import numbers
from tokenize import Number
from unicodedata import name
from urllib import request
# import urllib.request
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, status, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

class user(BaseModel):
    profile: str 
    name: str = Field(min_length=1, max_length=16)

class about(BaseModel):
    height : Optional[float]
    weight : Optional[float]


@app.get('/yourself')
async def yourself(request: Request):    
    context = {'request': request}
    return templates.TemplateResponse("yourself.html",context)


@app.post('/yourself')
async def yourself(request: Request, userName: str = Body(...), img: UploadFile = File(...)):    
    result = ({
        'name': userName,
        'img': img
    })
    context = {'request': request, 'result': result}
    print(result['name'])
    # result = Profile.insert_one(result)
    return templates.TemplateResponse("yourself.html",context)



@app.get('/heightWeight')
async def heightWeight(request: Request):    
    context = {'request': request}          
    return templates.TemplateResponse("heightWeight.html",context)


@app.post("/heightWeight")
async def heightWeight(request: Request,height: float = Form(...), weight: float = Form(...)):
    result = ({
        'Height': height,
        'Weight': weight
    })
    print(result['Height'])
    print(result['Weight'])
    context = {'request': request}       
    return result
    