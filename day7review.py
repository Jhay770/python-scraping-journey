import requests
from bs4 import BeautifulSoup
url ="https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")


all_books = []


for article in articles:
    title = article.find("h3").find("a")["title"]
    price = article.find("p", class_="price_color").text
    rating = article.find("p",class_="star-rating")["class"][1]
    in_stock = article.find("p", class_="instock availability").text.strip()

    book = {
    "title": title,
    "price": price,
    "rating": rating,
    "availability": in_stock
}
    all_books.append(book)
    print(f"title: {title}")
    print(f"price: {price}")
    print(f"rating: {rating}")
    print(f"availability: {in_stock}")
    print("............................")
    

print(f"total books scraped: {len(all_books)}")

    
    
    
