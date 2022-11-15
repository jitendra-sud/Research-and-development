from fastapi import APIRouter, Request
from app import schemas
from app.repository import feedback, notification
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=['Notification']
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/profileNotification",response_model = schemas.ShowPersonalDetails)
def show(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileNotification.html",context)


@router.get("/today", response_model = schemas.notification)
def get_today(id:str):
    return notification.get_today(id)

# @router.get("/this_week", response_model = schemas.ShowFeedback)
# def create(id:str, request: schemas.Feedback):
#     return feedback.create(id, request)

# @router.get("/last_week", response_model = schemas.ShowFeedback)
# def create(id:str, request: schemas.Feedback):
#     return feedback.create(id, request)
