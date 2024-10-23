# src/main.py
from scraper.scraper import scrape_product_data
from db.mongo_connector import store_product

# URL of the product to scrape
product_url = "https://www.onitsukatiger.com/jp/en-gl/product/mexico-66-cactful-s/1183c347_700.html"

def main():
    product_data = scrape_product_data(product_url)
    
    if product_data:
        store_product(product_data)
    else:
        print("Failed to scrape product data.")

if __name__ == "__main__":
    main()
