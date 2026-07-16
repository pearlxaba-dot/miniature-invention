# miniature-invention
Stats SA economic datasets 
import requests

url = "https://githubusercontent.com"
response = requests.get(url)

if response.status_code == 200:
    stats_data = response.json()  # Use response.text if it is a text file
    print(stats_data)
else:
    print(f"Failed to retrieve file. Status code: {response.status_code}")

