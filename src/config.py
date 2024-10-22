import os

# Configuration settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "product_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "onitsuka_tiger_products")
PRODUCT_SOURCE_URL = "https://www.onitsukatiger.com"
