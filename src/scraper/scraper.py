import requests
from bs4 import BeautifulSoup
from src.scraper.translator import translate


def scrape_product_data(product_url):
    """
    Scrape product data from a given product URL.
    """
    try:
        # Send request to product page
        response = requests.get(product_url)
        if response.status_code != 200:
            print(f"Failed to fetch product page: {response.status_code}")
            return

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract product details
        title = soup.find('h1', class_='product-title').get_text(strip=True)
        description = soup.find('div', class_='product-description').get_text(strip=True)
        price = soup.find('span', class_='product-price').get_text(strip=True)
        variants = [variant.get_text(strip=True) for variant in soup.select('.product-variant')]
        stock_quantity = soup.find('span', class_='stock-quantity').get_text(strip=True)
        image_urls = [img['src'] for img in soup.find_all('img', class_='product-image')]

        # Translate the title and description
        title_en = translate(title)
        description_en = translate(description)

        # Structured product data
        product_data = {
            "title": title_en,
            "description": description_en,
            "price": price,
            "variants": variants,
            "stock_quantity": stock_quantity,
            "images": image_urls
        }

        return product_data

    except Exception as e:
        print(f"Error scraping product data: {e}")
        return None
