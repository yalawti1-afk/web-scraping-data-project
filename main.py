import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://books.toscrape.com/"

def scrape_books(url):
    response = requests.get(
        url,
        timeout=20,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        title = book.h3.a.get("title", "").strip()
        price = book.select_one(".price_color").get_text(strip=True)
        availability = book.select_one(".availability").get_text(strip=True)

        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

    return books


if __name__ == "__main__":
    try:
        data = scrape_books(URL)

        if not data:
            print("No books found.")
        else:
            df = pd.DataFrame(data)
            df.to_csv("books.csv", index=False, encoding="utf-8-sig")

            print(f"Successfully collected {len(df)} books.")
            print(df.head())
            print("Data saved to books.csv")

    except requests.RequestException as error:
        print(f"Request failed: {error}")
