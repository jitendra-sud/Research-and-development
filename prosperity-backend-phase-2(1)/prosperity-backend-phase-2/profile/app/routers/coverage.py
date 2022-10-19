from fastapi import APIRouter
from app import schemas 
from app.repository import personal_details, coverage

router = APIRouter(
    prefix="/coverage",
    tags=['Coverage']
)

@router.post("/buy_policy", response_model=schemas.Coverage)
def create(id:str, request: schemas.Coverage):
    return coverage.create(id, request)


@router.get("/protection")
def show(id: str):
    return coverage.protection(id)

@router.get("/investment", response_model = schemas.ShowPersonalDetails)
def show(id: str):
    return coverage.investment(id)
