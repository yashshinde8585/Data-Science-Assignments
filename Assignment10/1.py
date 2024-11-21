# 1) use following url to extract data 
# https://jovian.com/outlink?url=http%3A%2F%2Fbooks.toscrape.com

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    print(f"Title: {title}, Price: {price}")
