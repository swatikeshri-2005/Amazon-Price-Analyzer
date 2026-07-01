import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

def scrape_products(search_term, pages=3):

    data = []

    for page in range(1, pages + 1):

        print(f"Scraping page {page}...")

        url = f"https://www.amazon.in/s?k={search_term}&page={page}"

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)

            if response.status_code != 200:
                print(f"Failed to fetch page {page}. Status Code: {response.status_code}")
                continue

            soup = BeautifulSoup(response.content, "lxml")

            products = soup.select(
                "div[data-component-type='s-search-result']"
            )

            print(f"Found {len(products)} products")

            for p in products:

                title = p.select_one("h2 span")
                price = p.select_one("span.a-price-whole")
                rating = p.select_one("span.a-icon-alt")

                data.append({
                    "Title": title.get_text(strip=True) if title else None,
                    "Price": price.get_text(strip=True) if price else None,
                    "Rating": rating.get_text(strip=True) if rating else None
                })

            time.sleep(2)

        except Exception as e:
            print("Error:", e)

    df = pd.DataFrame(data)

    # Create output folder automatically
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "data", "raw")

    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "amazon_products.csv")

    df.to_csv(output_file, index=False)

    print("\nData saved successfully!")
    print(f"Location: {output_file}")
    print(f"Total records: {len(df)}")

    print("\nSample Data:")
    print(df.head())


if __name__ == "__main__":
    scrape_products("laptop")