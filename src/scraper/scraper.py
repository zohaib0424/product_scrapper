import re
import requests
from bs4 import BeautifulSoup

def scrape_product_data(product_url):
    response = requests.get(product_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        print({soup})
        
        # Find the script tag that contains the product data
        script_tag = soup.find('script', text=re.compile('magentoStorefrontEvents.context.setProduct'))
                
        if script_tag:
            script_content = script_tag.string
            
            product_data = {}
            name_match = re.search(r'"name":"(.*?)"', script_content)
            if name_match:
                product_data['name'] = name_match.group(1)
            
            id_match = re.search(r'"productId":(\d+)', script_content)
            if id_match:
                product_data['productId'] = id_match.group(1)
            
            sku_match = re.search(r'"sku":"(.*?)"', script_content)
            if sku_match:
                product_data['sku'] = sku_match.group(1)
            
            url_match = re.search(r'"canonicalUrl":"(.*?)"', script_content)
            if url_match:
                product_data['canonicalUrl'] = url_match.group(1).replace('\\/', '/')
            
            categories_match = re.search(r'"categories":\[(.*?)\]', script_content)
            if categories_match:
                categories = re.findall(r'"(.*?)"', categories_match.group(1))
                product_data['categories'] = categories
            
            pricing_match = re.search(r'"pricing":(.*?)}', script_content)
            if pricing_match:
                product_data['pricing'] = pricing_match.group(1)
            
            image_url_match = re.search(r'"mainImageUrl":"(.*?)"', script_content)
            if image_url_match:
                product_data['mainImageUrl'] = image_url_match.group(1).replace('\\/', '/')
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
