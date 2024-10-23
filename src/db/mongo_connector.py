from pymongo import MongoClient
from pymongo.server_api import ServerApi

URI = "mongodb+srv://zohaibkhattak6:Qk3ewCUfFumPMHnG@cluster0.tmfxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME='product_scraper'
COLLECTION_NAME='products'

def get_db_connection():
    try:
        client = MongoClient(URI, server_api=ServerApi('1'))
        db = client[DB_NAME]
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def store_product(product_data):
    db = get_db_connection()
    
    if db is not None:
        existing_product = db[COLLECTION_NAME].find_one({"productId": product_data['productId']})
        
        if existing_product:
            print("Product already exists in the database.")
        else:
            collection = db[COLLECTION_NAME]
            try:
                result = collection.insert_one(product_data)
                print(f"Product inserted with ID: {result.inserted_id}")
            except Exception as e:
                print(f"Error inserting product data: {e}")
    else:
        print("Failed to connect to the database.")
