from dotenv import load_dotenv
import pymongo
import os

load_dotenv()
DB = os.getenv("DATABASE_URL")
myClient = pymongo.MongoClient(DB)
database = myClient['TaskManager']
user = database['users']
notes = database['notes']