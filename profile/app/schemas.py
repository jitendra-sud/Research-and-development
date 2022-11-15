from typing import List, Optional
from unittest.util import _MAX_LENGTH
from pydantic import BaseModel, constr, EmailStr, Field
from enum import Enum
from bson import ObjectId
from typing import Optional
from fastapi import Form
from datetime import date
from pydantic.types import PaymentCardBrand, PaymentCardNumber


MobileStr = constr(regex = r'^\d{10}$') 
cvvStr =constr(regex="^[0-9]{3,4}$")
expiryDateStr = constr(regex="^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$")
upiIdStr= constr(regex="^[\w.-]+@[\w.-]+$")
upiIdStr = constr(regex = "[a-zA-Z0-9\\.\\-]{2,256}\\@[a-zA-Z][a-zA-Z]{2,64}")
nameStr = constr(regex=r"^([A-Za-z]+)( [A-Za-z]+)*( [A-Za-z]+)*$", max_length=30)

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

@form_body
class Item(BaseModel):
    name: str = Field(max_length=30, regex=r"^([A-Za-z]+)( [A-Za-z]+)?( [A-Za-z]+)$")
    profession: str = Field(max_length = 20)
    number: MobileStr
    email: EmailStr

class notification(BaseModel):
    property: str
    time:str
    message:str
    info:str
    
class Coverage(BaseModel):
    policyName: str
    sumAssured:int
    premium:int
    dueDate:str
    status:str

class showCoverage(Coverage):
    class Config:
        orm_mode=True

class Feedback(BaseModel):
    rating: int = Field(gt=0,lt=6)
    title: str = Field(max_length = 20)
    comment: str = Field(max_length = 200)

class ShowFeedback(BaseModel):
    rating: int 
    title: str 
    comment: str
    class Config():
        orm_mode = True

class PersonalDetails(BaseModel):
    name: str = Field(max_length=30, regex=r"^([A-Za-z]+)( [A-Za-z]+)?( [A-Za-z]+)$")
    profession: str = Field(max_length = 20)
    mobile: MobileStr
    email: EmailStr

class ShowPersonalDetails(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias='_id')
    name: str 
    profession: str 
    mobile: int 
    email: str

    class Config():
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class AddBank(str, Enum):
    union_bank = "Union bank"
    axis = "Axis Bank"
    icici = "ICICI"
    hdfc = "HDFC"
    sbi = "SBI"


class AddCard(BaseModel):
    name_on_card : str
    card_number : int  #only validates credit card
    expiry_date : expiryDateStr
    cvv : cvvStr


class upiId(BaseModel):
    upiId: upiIdStr


class Card(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    number: PaymentCardNumber
    exp: date

    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < date.today()

# card = Card(
#     name='Georg Wilhelm Friedrich Hegel',
#     number='4000000000000002',
#     exp=date(2023, 9, 30)
# )

# assert card.number.brand == PaymentCardBrand.visa
# assert card.number.bin == '400000'
# assert card.number.last4 == '0002'
# assert card.number.masked == '400000******0002'