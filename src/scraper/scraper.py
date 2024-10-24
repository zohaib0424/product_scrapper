import re
import requests
from bs4 import BeautifulSoup
import json


def get_response(url):
    """Fetch the response from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None


def extract_gallery_data(gallery_script):
    """Extract image data from the gallery script."""
    try:
        script_content = gallery_script.string
        parsed_data = json.loads(script_content)
        images_data = parsed_data["[data-gallery-role=gallery-placeholder]"]["mage/gallery/gallery"]["data"]
        return images_data
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Failed to extract gallery data: {e}")
        return []  # Return empty list if extraction fails


def extract_swatch_options(extra_script):
    """Extract size and color options from the swatch options script."""
    try:
        script_content = extra_script.string
        json_data = re.search(r'\{.*\}', script_content).group(0)
        json_obj = json.loads(json_data)

        sizes = json_obj.get("attributes", {}).get("558", {}).get("options", [])
        colors = json_obj.get("attributes", {}).get("277", {}).get("options", [])
        return sizes, colors
    except (json.JSONDecodeError, AttributeError) as e:
        print(f"Failed to extract size data: {e}")
        return [], []  # Return empty lists if extraction fails


def extract_product_info(product_script_tag):
    """Extract product information from the product script tag."""
    product_info = {}
    try:
        script_content = product_script_tag.string
        product_info['name'] = re.search(r'"name":"(.*?)"', script_content).group(1)
        product_info['productId'] = re.search(r'"productId":(\d+)', script_content).group(1)
        product_info['sku'] = re.search(r'"sku":"(.*?)"', script_content).group(1)
        product_info['canonicalUrl'] = re.search(r'"canonicalUrl":"(.*?)"', script_content).group(1).replace('\\/', '/')
        categories_match = re.search(r'"categories":\[(.*?)\]', script_content)
        product_info['categories'] = re.findall(r'"(.*?)"', categories_match.group(1)) if categories_match else []
        pricing_match = re.search(r'"pricing":(.*?)}', script_content)
        product_info['pricing'] = pricing_match.group(1) if pricing_match else {}
        product_info['mainImageUrl'] = re.search(r'"mainImageUrl":"(.*?)"', script_content).group(1).replace('\\/', '/') if re.search(r'"mainImageUrl":"(.*?)"', script_content) else None

        return product_info
    except (AttributeError, json.JSONDecodeError) as e:
        print(f"Failed to extract product info: {e}")
        return {}  # Return empty dict if extraction fails


def scrape_product_data(product_url):
    """Main function to scrape product data from the given URL."""
    response = get_response(product_url)
    if not response:
        return None
    else:
     print("Script tag not found.")
    
    product_data = {}
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print('here is the soup',soup)

    product_script_tag = soup.find('script', text=re.compile('magentoStorefrontEvents.context.setProduct'))
    script_tags = soup.find_all('script', {'type': 'text/x-magento-init'})
    
    if product_script_tag:
        product_info = extract_product_info(product_script_tag)
        product_data.update(product_info)
            
    extra_product_script_tag = None
    gallery = None

    for script in script_tags:
        if 'data-role=swatch-options' in script.text:
            extra_product_script_tag = script
        if 'data-gallery-role=gallery-placeholder' in script.text and "mage/gallery/gallery" in script.text:
            gallery = script

    # Extract gallery data
    if gallery:
        product_data['images'] = extract_gallery_data(gallery)

    # Extract swatch options
    if extra_product_script_tag:
        sizes, colors = extract_swatch_options(extra_product_script_tag)
        product_data['sizes'] = sizes
        product_data['colors'] = colors
    else:
        print("No swatch-options script tag found.")
        product_data['sizes'] = []
        product_data['colors'] = []

    return product_data if product_data else None

