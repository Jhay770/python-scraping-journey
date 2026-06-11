import requests
from bs4 import BeautifulSoup
import csv

all_books = []

for page in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Scrapping page {page}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h3").find("a")["title"]
        price = article.find("p", class_="price_color").text
        rating = article.find("p", class_="star-rating")["class"][1]
        in_stock = article.find("p", class_="instock availability").text.strip()


        book = {
            "title": title,
            "price": price,
            "rating": rating,
            "availability": in_stock
        }
        all_books.append(book)

with open("all_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price", "rating", "availability"])
    writer.writeheader()
    writer.writerows(all_books)

print(f"Done! Total books scraped: {len(all_books)}")

        
        
    

