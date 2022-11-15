from urllib import request
from fastapi import HTTPException, status, UploadFile, File
from app import schemas
from app.db import collection_users, collection_aadhar,collection_pan, collection_coverage
import uuid
import bson
from bson.binary import Binary
from bson import ObjectId


def create(id, request):
    data = dict(request)
    # user = collection_users.insert_one(data)
    # print(user.inserted_id)
    user = collection_users.find_one({"_id": ObjectId(id)})
    if "coverage" in user:
        cov = collection_users.find_one({"_id": ObjectId(user["coverage"])})
        cov["list"].append(data)
        return request
    data_dict = {
        "list" : [data] 
    }
    cov = collection_coverage.insert_one(data_dict)
    cov_id = cov.inserted_id
    user = collection_users.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": {
            "coverage":cov_id
        }
    })

    return request

def protection(id):
    response=dict()
    response["name"] = "SUD life Abhay"
    response["sum_assured"] = 725000
    response["premium"] = 7220
    response["status"] = "10/18"
    response["due"] = "24/02/22"

    all = [response]

    response["name"] = "SUD life Saral Jeevan"
    response["sum_assured"] = 525000
    response["premium"] = 7220
    response["status"] = "4/7"
    response["due"] = "24/02/22"

    all.append(response)
    
    return all

def investment(id):
    response=dict()
    response["name"] = "SUD life E-Wealth Royale "
    response["sum_assured"] = 225000
    response["premium"] = 6220
    response["status"] = "10/18"
    response["due"] = "24/02/22"

    all = [response]

    return response






