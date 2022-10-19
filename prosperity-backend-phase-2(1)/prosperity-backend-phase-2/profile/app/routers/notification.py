from fastapi import APIRouter
from app import schemas
from app.repository import feedback, notification

router = APIRouter(
    prefix="/notification",
    tags=['Notification']
)

@router.get("/today", response_model = schemas.notification)
def get_today(id:str):
    return notification.get_today(id)

# @router.get("/this_week", response_model = schemas.ShowFeedback)
# def create(id:str, request: schemas.Feedback):
#     return feedback.create(id, request)

# @router.get("/last_week", response_model = schemas.ShowFeedback)
# def create(id:str, request: schemas.Feedback):
#     return feedback.create(id, request)
