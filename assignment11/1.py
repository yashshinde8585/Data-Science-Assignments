# 1) Write a Python program to download and display the content of robot.txt for en.wikipedia.org.

import requests

def get_robots_txt(url):
    try:
       
        robots_url = f"{url}/robots.txt"
        response = requests.get(robots_url)
        
    
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to retrieve robots.txt, status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"


url = "https://en.wikipedia.org"
robots_content = get_robots_txt(url)
print(robots_content)
