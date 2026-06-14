import requests
from bs4 import BeautifulSoup
import csv

all_books = []

for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}"
    print(f"Scraping page {page}...")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("div", class_="quote")
    
    for article in articles:
        title = article.find("span", class_="text").text
        author = article.find("small", class_="author").text
        tags = article.find_all("a", class_="tag")
        tag_list = ", ".join([t.text for t in tags])
                
        book = {
            "title": title,
            "author": author,
            "tag": tag_list,
            
        }
        all_books.append(book)

with open("all_books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "author", "tag"])
    writer.writeheader()
    writer.writerows(all_books)

print(f"Done! Total books scraped: {len(all_books)}")
