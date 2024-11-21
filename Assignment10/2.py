#2)Write a Python program to extract h1 tags and image tags and extract source attribute from image tag.

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

h1_tags = soup.find_all("h1")
for h1 in h1_tags:
    print("H1 Tag:", h1.text)


img_tags = soup.find_all("img")
for img in img_tags:
    print("Image Source:", img.get("src"))
 
