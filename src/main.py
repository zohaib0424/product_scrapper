from src.scraper.scraper import scrape_product_data
from src.db.mongo_connector import save_to_mongo


if __name__ == '__main__':
    product_url = 'https://www.onitsukatiger.com/product-page'  # Replace with the actual product URL
    product_data = scrape_product_data(product_url)

    if product_data:
        save_to_mongo(product_data)
