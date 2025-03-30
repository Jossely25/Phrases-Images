import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GMAIL_USER = os.getenv("GMAIL_USER")
    GMAIL_PASS = os.getenv("GMAIL_PASS")
    SEND_TIME = os.getenv("SEND_TIME") 

