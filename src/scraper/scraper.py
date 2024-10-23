import re
import requests
from bs4 import BeautifulSoup

def scrape_product_data(product_url):
    response = requests.get(product_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the script tag that contains the product data
        script_tag = soup.find('script', text=re.compile('magentoStorefrontEvents.context.setProduct'))
        
        print({script_tag})
        
        if script_tag:
            # Extract the script content
            script_content = script_tag.string
            
            # Extract product data using regex
            product_data = {}
            
            # Extract product name
            name_match = re.search(r'"name":"(.*?)"', script_content)
            if name_match:
                product_data['name'] = name_match.group(1)
            
            # Extract product ID
            id_match = re.search(r'"productId":(\d+)', script_content)
            if id_match:
                product_data['productId'] = id_match.group(1)
            
            # Extract SKU
            sku_match = re.search(r'"sku":"(.*?)"', script_content)
            if sku_match:
                product_data['sku'] = sku_match.group(1)
            
            # Extract canonical URL
            url_match = re.search(r'"canonicalUrl":"(.*?)"', script_content)
            if url_match:
                # Canonical URL contains escaped slashes, so we need to unescape them
                product_data['canonicalUrl'] = url_match.group(1).replace('\\/', '/')
            
            # If all data was found, return it as a single object
            if product_data:
                print(f"Scraped product data: {product_data}")
                return product_data
            else:
                print("No product data found.")
                return None
        else:
            print("Script tag not found.")
            return None
    else:
        print(f"Failed to retrieve page: Status code {response.status_code}")
        return None
