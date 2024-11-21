# 4) Write a Python program to extract h1 tag from example.com.

import requests
from bs4 import BeautifulSoup

def extract_h1_tag(url):
    try:
       
        response = requests.get(url)
        
       
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
          
            h1_tag = soup.find('h1')
            
          
            if h1_tag:
                return h1_tag.text.strip()
            else:
                return "No <h1> tag found."
        else:
            return f"Failed to retrieve data, status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

url = "http://example.com"
h1_content = extract_h1_tag(url)
print(f"<h1> tag content: {h1_content}")
