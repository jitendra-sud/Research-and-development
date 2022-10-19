from pymongo import MongoClient

# by default connect to the local host
conn = MongoClient(
    'mongodb+srv://srija:EIbN4LlyqFyRZfcQ@cluster0.jg7b3zi.mongodb.net/?retryWrites=true&w=majority')


db = conn.prosperity_profile

collection_users = db["users"]
collection_feedback = db["feedback"]
collection_aadhar = db["aadhar"]
collection_pan = db["pan"]
collection_cards = db["cards"]
collection_coverage = db["coverage"]