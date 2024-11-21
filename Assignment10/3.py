# 3) Write a Python program to extract and display all the header and paragraph tags

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

for i in range(1, 7):
    headers = soup.find_all(f"h{i}")
    for header in headers:
        print(f"H{i} Tag:", header.text)


paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print("Paragraph:", paragraph.text)
