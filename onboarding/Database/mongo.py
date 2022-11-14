from enum import unique
from pymongo import mongo_client
import pymongo
from config import settings

client = mongo_client.MongoClient(
    settings.DATABASE_URL, serverSelectionTimeoutMS=5000)

try:
    conn = client.server_info()
    print(f'Connected to MongoDB Server {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
Profile = db.profile_picture
Bmi = db.bmi



#we can use this for unique username
#User.create_index([("email", pymongo.ASCENDING)], unique=True)
#Bmi.create_index([("height" ,pymongo.ASCENDING)],unique=True)



