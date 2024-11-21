# 3) Write a Python program to display the name of the most recently added dataset on data.gov.

import requests

def get_most_recent_dataset():
    try:
        
        url = "https://catalog.data.gov/api/3/action/package_search"
        
     
        params = {
            "sort": "metadata_created desc", 
            "rows": 1                         
        }
        
    
        response = requests.get(url, params=params)
        
       
        if response.status_code == 200:
            data = response.json()
            if data['result']['results']:
               
                most_recent_dataset = data['result']['results'][0]['title']
                return most_recent_dataset
            else:
                return "No datasets found."
        else:
            return f"Failed to retrieve data, status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

most_recent_dataset = get_most_recent_dataset()
print(f"Most recently added dataset: {most_recent_dataset}")
