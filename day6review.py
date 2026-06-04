import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")
for article in articles:
    title = article.find("h3").find("a")["title"]
    price = article.find("p", class_="price_color").text
    print(f"{title} - {price}")
    
