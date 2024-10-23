from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection URI for Atlas
uri = "mongodb+srv://zohaibkhattak6:Qk3ewCUfFumPMHnG@cluster0.tmfxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def get_db_connection():
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['product_scraper']
        return db
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def store_product(product_data):
    # Connect to the database using the get_db_connection function
    db = get_db_connection()
    
    # Check if the connection was successful
    if db is not None:
        # Insert product data into a collection
        collection = db['products']
        try:
            result = collection.insert_one(product_data)
            print(f"Product inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error inserting product data: {e}")
    else:
        print("Failed to connect to the database.")
