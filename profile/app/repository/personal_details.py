from urllib import request
from fastapi import HTTPException, status
from app import schemas
from app.db import collection_users
import re
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

def show(id):
    user = collection_users.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} does not exist.')
    # print(user)
    return user

def create(request):
    data = jsonable_encoder(request)
    user = collection_users.find_one({"email": request.email})
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Email already exists.')
                            
    # remove extra spaces from name                            
    data["name"] = re.sub(' +', ' ', data["name"])
    user = collection_users.insert_one(data)
    print(user.inserted_id)
    user = collection_users.find_one({"_id": ObjectId(user.inserted_id)})
    return user 

def update(id, request):
    user = collection_users.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(request)
    })
    return user