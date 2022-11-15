from fastapi import APIRouter, Request
from app import schemas 
from app.repository import personal_details, coverage
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")


router = APIRouter(
    prefix="",
    tags=['Coverage']
)

@router.get("/profileCoverage",response_model = schemas.ShowPersonalDetails)
def show(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profileCoverage.html",context)

@router.post("/buy_policy", response_model=schemas.Coverage)
def create(id:str, request: schemas.Coverage):
    return coverage.create(id, request)


# @router.get("/protection")
# def show_protect(id: str):
#     return coverage.protection(id)

# @router.get("/investment", response_model = schemas.ShowPersonalDetails)
# def show_invest(id: str):
#     return coverage.investment(id)
