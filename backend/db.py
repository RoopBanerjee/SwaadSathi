from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["swaadsathi"]
users_collection = db["users"]

def save_user_to_db(user_data):
    existing_user = users_collection.find_one({"uid": user_data["uid"]})
    if not existing_user:
        users_collection.insert_one(user_data)
