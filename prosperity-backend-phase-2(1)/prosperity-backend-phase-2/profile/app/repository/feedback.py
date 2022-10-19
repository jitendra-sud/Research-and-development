
from bson import ObjectId
from fastapi import HTTPException, status
from app import schemas
from app.db import collection_feedback, collection_users
from bson import ObjectId

def create(id, request):
    data = dict(request)
    data = collection_feedback.insert_one(data)
    feedback_id = data.inserted_id
    user = collection_users.find_one({"_id": ObjectId(id)})
    if "feedbacks" in user:
        user["feedbacks"].append(feedback_id)
    else:
        user["feedbacks"]=[feedback_id]
    collection_users.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": user
    })
    data = collection_feedback.find_one({"_id": ObjectId(feedback_id)})
    print(data)
    return data
