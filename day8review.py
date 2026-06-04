import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
bodies = soup.find_all("div", class_="quote")

for body in bodies:
    title = body.find("span", class_="text").text
    author = body.find("small", class_="author").text

    books = {
    "Title": title,
    "Author": author
}
    
    print(f"Title: {title}")
    print(f"Author: {author}")
    print("...................")
