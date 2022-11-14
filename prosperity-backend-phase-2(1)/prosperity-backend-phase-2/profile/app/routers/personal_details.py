from fastapi import APIRouter
from app import schemas
from app.repository import personal_details
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, status, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter(
    prefix="",
    tags=['Personal details']
)


templates = Jinja2Templates(directory="app/templates")

@router.get("/profileDetails", response_model = schemas.ShowPersonalDetails)
async def show( request: Request):
    # user = personal_details.show(id)
    user = ({})
    # user = ({
    #     'name': "jitu",
    #     'number': 7667287827,
    #     'email': "jitu@gmial.com",
    #     'profession': "SDE"
    # })
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileDetails.html",context)

@router.post("/profileDetails")
async def create(request: Request):
    form = await request.form()
    errors = []
    user = ({
        'name': form.get("name"),
        'number': form.get("number"),
        'email': form.get("email"),
        'profession': form.get("profession")
    })
    
    print(user["email"])
    context = {'request':request, 'user': user}    
    return templates.TemplateResponse("profiles/profileDetails.html",context)

# @router.get("/show", response_model = schemas.ShowPersonalDetails)
# def show(id:str):
#     user = personal_details.show(id)
#     # user['name']
#     return personal_details.show(id)

# @router.get("/show", response_model = schemas.ShowPersonalDetails)
# def show(id:str, request: Request):
#     context = {'request': request, 'id':id}
#     return templates.TemplateResponse("profileAbout.html",context)

@router.post("/create", response_model = schemas.ShowPersonalDetails)
def create(request: schemas.PersonalDetails):
    return personal_details.create(request)

@router.put("/update", response_model=schemas.ShowPersonalDetails)
def update(id:str, request: schemas.PersonalDetails):
    return personal_details.update(id, request)

# required oninvalid="this.setCustomValidity('Name can not be empty..')"
# required oninvalid="this.setCustomValidity('profession can not be empty..')"
# required oninvalid="this.setCustomValidity('Mobile Number should be 10-digits..')"




# var pro = document.forms["form"]["profession"].value;
#         var num = document.forms["form"]["number"].value;
#         var email = document.forms["form"]["email"].value;


#         if (name==null || name==""){  
#             alert("Name can't be blank");
#             return false;
#           }else if(pro==null || pro=""){  
#             alert("Profession can't be blank");  
#             return false;
#             }else if(num.length != 10){
#                 alert("Mobile Nubmber should be of 10-Digits")
#                 return false;
#             }  