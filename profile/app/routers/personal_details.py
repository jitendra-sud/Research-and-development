from urllib.request import Request
from fastapi import APIRouter, status, Request, Form, Depends
from app import schemas
from app.repository import personal_details
import os
from pathlib import Path
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=['Personal details']
)

templates = Jinja2Templates(directory="app/templates")

@router.get("/profileDetails", response_model = schemas.ShowPersonalDetails)
async def show( request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileDetails.html",context)

@router.post("/profileDetails", status_code=status.HTTP_201_CREATED, response_model = schemas.ShowPersonalDetails )
async def create(request: Request):
    form = await request.form()
    user = ({
        'name': form.get("name"),
        'number': form.get("number"),
        'email': form.get("email"),
        'profession': form.get("profession")
    })
    
    print(user["email"])

    context = {'request':request, 'user': user}    
    return templates.TemplateResponse("profiles/profileDocuments.html",context)


@router.put("/update", response_model=schemas.ShowPersonalDetails)
def update(id:str, request: schemas.PersonalDetails):
    return personal_details.update(id, request)
