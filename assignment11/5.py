# 5) Write a Python program to extract and display all the image links from en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer).


import requests
from bs4 import BeautifulSoup

def extract_image_links(url):
    try:
        
        response = requests.get(url)
        
    
        if response.status_code == 200:
          
            soup = BeautifulSoup(response.text, 'html.parser')
            
           
            images = soup.find_all('img')
            image_links = []
            for img in images:
               
                img_url = img.get('src')
                if img_url:
                    if img_url.startswith("//"):
                        img_url = "https:" + img_url
                    elif not img_url.startswith("http"):
                        img_url = url + img_url  
                    image_links.append(img_url)
            return image_links
        else:
            return f"Failed to retrieve data, status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"


url = "https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)"
image_links = extract_image_links(url)


print("Image links found on the page:")
for link in image_links:
    print(link)
