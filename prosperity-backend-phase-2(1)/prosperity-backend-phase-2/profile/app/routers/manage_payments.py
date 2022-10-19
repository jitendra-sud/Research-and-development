from pydoc import describe
from fastapi import APIRouter, HTTPException, status
from app import schemas
from app.db import collection_cards
from app import card_number
router = APIRouter(
    prefix="/payments",
    tags=['Manage Payments']
)

@router.post("/bank", response_model = schemas.AddBank)
def add_bank(id:str, request: schemas.AddBank):
    return request

@router.post("/card", response_model = schemas.AddBank)
def add_card(id:str, request:schemas.AddCard):
    if card_number.validate_card(request.card_number):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid card number.")
    
    collection_cards.insert_one(dict(request))
    return "Added Succesfully."

@router.post("/bank", response_model = schemas.AddBank)
def add_bank(id:str, request: schemas.AddBank):
    return request

@router.post("/add_upi_id")
def add_upi(id:str, upi_id:schemas.upiIdStr):
    return {"UPI verified!"}
