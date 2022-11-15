from pymongo import MongoClient
from app.config import settings
# by default connect to the local host
conn = MongoClient(
    settings.DATABASE_URL)


db = conn.prosperity_profile

collection_users = db["users"]
collection_feedback = db["feedback"]
collection_aadhar = db["aadhar"]
collection_pan = db["pan"]
collection_cards = db["cards"]
collection_coverage = db["coverage"]