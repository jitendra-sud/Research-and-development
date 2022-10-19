from fastapi import APIRouter
from app import schemas
from app.repository import personal_details
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, status, Body
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter(
    prefix="/details",
    tags=['Personal details']
)


templates = Jinja2Templates(directory="app/templates")
# router.mount(
#     "/static",
#     StaticFiles(directory="app/static"),
#     name="static",
# )

@router.get("/profileDetails", response_model = schemas.ShowPersonalDetails)
async def show( request: Request):
    context = {'request': request}
    return templates.TemplateResponse("profileDetails.html",context)

# @app.post("/profileDetails")
# async def create(request: Request, name: str = Form(...), number: int = Form(...), email: str = Form(...), profession: str = Form(...) ):
#     result = ({
#         'name': name,
#         'number': number,
#         'email': email,
#         'profession': profession
#     })
#     # context = {'request':request, 'result':result}
#     return result


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
