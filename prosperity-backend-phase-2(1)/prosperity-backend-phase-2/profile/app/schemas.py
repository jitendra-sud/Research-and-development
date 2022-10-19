from typing import List, Optional
from unittest.util import _MAX_LENGTH
from pydantic import BaseModel, constr, EmailStr, Field
from enum import Enum
from bson import ObjectId
from typing import Optional

MobileStr = constr(regex = r'^\d{10}$') 
cvvStr =constr(regex="^[0-9]{3,4}$")
expiryDateStr = constr(regex="^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$")
upiIdStr= constr(regex="^[\w.-]+@[\w.-]+$")
upiIdStr = constr(regex = "[a-zA-Z0-9\\.\\-]{2,256}\\@[a-zA-Z][a-zA-Z]{2,64}")

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
    name: str = Field(max_length=30)
    profession: str = Field(max_length = 20)
    mobile: MobileStr
    email: EmailStr

class ShowPersonalDetails(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
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