from fastapi import APIRouter
from app import schemas
from app.repository import feedback

router = APIRouter(
    prefix="/feedback",
    tags=['Feedback']
)

@router.post("/create", response_model = schemas.ShowFeedback)
def create(id:str, request: schemas.Feedback):
    return feedback.create(id, request)
