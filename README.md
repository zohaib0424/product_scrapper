# product_scrapper# Product Scraper

This project scrapes product information from the Onitsuka Tiger website, translates it into English, and stores it in MongoDB.

## Features

- Scrape product title, description, price, variants, stock quantity, and images.
- Translate product details to English using Google Translator API.
- Store the scraped data in MongoDB.

## Prerequisites

- Python 3.x
- MongoDB

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/product_scraper.git
    cd product_scraper
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up MongoDB locally or configure a remote MongoDB instance. Modify `config.py` to include your MongoDB connection settings.

4. Run the scraper:
    ```bash
    python src/main.py
    ```

## Directory Structure

- `scraper/`: Contains scraping and translation logic.
- `db/`: Handles MongoDB connections and saving data.
- `config.py`: Contains database configuration settings.
- `main.py`: The entry point to the project.

## License

This project is licensed under the MIT License.
