import os

# Configuration settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://zohaibkhattak6:Qk3ewCUfFumPMHnG@cluster0.tmfxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "product_scraper")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "products")
