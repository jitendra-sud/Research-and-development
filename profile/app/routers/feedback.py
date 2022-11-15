from fastapi import APIRouter, Request
from app import schemas
from app.repository import feedback
from fastapi.responses import ORJSONResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    prefix="",
    tags=['Feedback'],
    default_response_class=ORJSONResponse
)

@router.get("/profileFeedback",response_model = schemas.ShowPersonalDetails)
def show(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileFeedback.html",context)

@router.get("/profileAbout",response_model = schemas.ShowPersonalDetails)
def show(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileAbout.html",context)



@router.post("/create", response_model = schemas.ShowFeedback)
def create(id:str, request: schemas.Feedback):
    return feedback.create(id, request)
