from pymongo import MongoClient, ASCENDING
from app.config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()  
db.users.create_index([("email", ASCENDING)], unique=True)

def get_db():
    return db
