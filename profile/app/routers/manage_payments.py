from pydoc import describe
from fastapi import APIRouter, HTTPException, status, Request, Body, Form
from app import schemas
from app.db import collection_cards
from app import card_number
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(
    prefix="",
    tags=['Manage Payments']
)

@router.get("/profilePayments",response_model = schemas.ShowPersonalDetails)
def show(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profilePayments.html",context)

@router.post("/profilePayments",response_model = schemas.ShowPersonalDetails)
def show(request: Request, upi_id: str = Body(...)) :
    context = {'request': request, 'upi_id': upi_id}
    return templates.TemplateResponse("profiles/profilePayments.html",context)



@router.get("/profilePaymentsAddCards",response_model = schemas.ShowPersonalDetails)
def show_cards(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profilePaymentsAddCards.html",context)

@router.post("/profilePaymentsAddCards",response_model = schemas.ShowPersonalDetails)
def create_cards(request: Request, name: str = Form(...), cvv: int = Form(...), card_number: int = Form(...), date: str = Form(...)) :
    user = ({
        'name': name,
        'cvv': cvv,
        'card_number': card_number,
        'date': date,
    })
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profilePayments.html",context)


@router.get("/profilePaymentsAddBanks",response_model = schemas.ShowPersonalDetails)
def show_bank(request: Request):
    user = ({})
    context = {'request': request, 'user': user}
    return templates.TemplateResponse("profiles/profilePaymentsAddBanks.html",context)



# @router.post("/bank", response_model = schemas.AddBank)
# def add_bank(id:str, request: schemas.AddBank):
#     return request

# @router.post("/card", response_model = schemas.Card)
# def add_card(id:str, request:schemas.Card):
#     collection_cards.insert_one(dict(request))
#     return request


# @router.post("/add_upi_id")
# def add_upi(id:str, upi_id:schemas.upiIdStr):
#     return {"UPI verified!"}
