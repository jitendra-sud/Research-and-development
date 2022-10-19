from urllib import request
from fastapi import HTTPException, status
from app import schemas
from app.db import collection_users

from bson import ObjectId


def show(id):
    user = collection_users.find_one({"_id": ObjectId(id)})
    print(user)
    return user

def create(request):
    data = dict(request)
    user = collection_users.insert_one(data)
    print(user.inserted_id)
    user = collection_users.find_one({"_id": ObjectId(user.inserted_id)})
    return user 


def update(id, request):
    user = collection_users.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(request)
    })
    return user