from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://127.0.0.1:27017/")
    return client["mydb"]