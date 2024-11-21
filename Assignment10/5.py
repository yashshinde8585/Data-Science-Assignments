# 5) write a program to extract hyperlinks in all anchor tags.

import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com"


response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

anchors = soup.find_all("a")
for anchor in anchors:
    href = anchor.get("href")
    if href:
        print("Hyperlink:", href)
