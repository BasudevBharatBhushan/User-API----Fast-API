from pymongo import MongoClient
from constants import DB_URL

client = MongoClient(host=DB_URL)
db = client.c3
user_collection = db.user
