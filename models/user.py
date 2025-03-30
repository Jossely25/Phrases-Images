from database.connection import db

def add_user(user_data):
    return db.users.insert_one(user_data)

def get_all_users():
    return list(db.users.find())

def get_user_by_email(email):
    return db.users.find_one({"email": email})
