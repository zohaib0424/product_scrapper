import pymongo
from src.config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME


def connect_to_mongo():
    """
    Connect to MongoDB.
    """
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    return collection


def save_to_mongo(product_data):
    """
    Save product data to MongoDB.
    """
    try:
        collection = connect_to_mongo()
        collection.insert_one(product_data)
        print("Product data saved successfully to MongoDB")
    except Exception as e:
        print(f"Error saving data to MongoDB: {e}")
