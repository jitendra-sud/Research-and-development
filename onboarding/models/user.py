from datetime import datetime,date
from bson.objectid import ObjectId
from enum import Enum
from pydantic import BaseModel,Field,validator
from email_validator import validate_email as validate_e,EmailNotValidError
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Body
from fastapi.params import File
from typing import List,Optional


class EmailField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> str:
        try:
            validate_e(v)
            return v
        except EmailNotValidError:
            raise ValueError("Email is not valid")


class Userbase(BaseModel):
    name: str = Field(min_length=1, max_length=16)

    @validator("name")
    def validate_full_name(cls, v):
        try:
            first_name, last_name = v.split()
            return v
        except Exception:
            raise ValueError("You should provide at least 2 names")