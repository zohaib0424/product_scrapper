import requests
from bs4 import BeautifulSoup
from .translator import translate_product

def scrape_product_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example of scraping product title, price, stock, and images
        title = soup.find('h1', class_='product-title').text
        price = soup.find('span', class_='product-price').text
        stock_status = "In Stock" if soup.find('span', class_='in-stock') else "Out of Stock"
        images = [img['src'] for img in soup.find_all('img', class_='product-image')]

        # Translate the title to English
        translated_title = translate_product(title)

        # Return the scraped data
        return {
            'title': translated_title,
            'price': price,
            'stock_status': stock_status,
            'images': images
        }
    except Exception as e:
        print(f"Error scraping product data: {e}")
        return None
