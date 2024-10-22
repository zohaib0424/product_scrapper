# src/db/mongo_connector.py
from pymongo import MongoClient

def get_db_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client['product_scraper']
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def store_product(product_data):
    db = get_db_connection()
    if db:
        try:
            products_collection = db['products']
            products_collection.insert_one(product_data)
            print("Product data successfully stored in the database.")
        except Exception as e:
            print(f"Error storing product data: {e}")
