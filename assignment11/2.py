# 2) Write a Python program to get the number of datasets currently listed on data.gov.

import requests

def get_datasets_count():
    try:
       
        url = "https://catalog.data.gov/api/3/action/package_search"
        
       
        response = requests.get(url)
        
       
        if response.status_code == 200:
            data = response.json()
           
            datasets_count = data['result']['count']
            return datasets_count
        else:
            return f"Failed to retrieve data, status code: {response.status_code}"
    except requests.RequestException as e:
        return f"An error occurred: {e}"


count = get_datasets_count()
print(f"Number of datasets on data.gov: {count}")
