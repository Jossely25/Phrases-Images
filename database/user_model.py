from database.connection import get_db
from pymongo.errors import DuplicateKeyError

def create_user(data):
    db = get_db()
    users_collection = db.users
    try:

        users_collection.insert_one(data)
    except DuplicateKeyError:

        return False  

    return True 

def get_user_by_email(email):
    db = get_db()
    users_collection = db.users
    return users_collection.find_one({"email": email})
