import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
bodies = soup.find_all("div", class_="quote")

all_quotes = []

for body in bodies:
    title = body.find("span", class_="text").text
    author = body.find("small", class_="author").text
    
    quote = {
        "title": title,
        "author": author
    }
    all_quotes.append(quote)

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "author"])
    writer.writeheader()
    writer.writerows(all_quotes)

print("Data saved to quotes.csv!")
