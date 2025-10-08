import requests
import json

url = "https://openlibrary.org/search/authors.json?q=jenny%20han"

response = requests.get(url)

data = response.json()

with open("author1.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

url = "https://openlibrary.org/search/authors.json?q=f%20scott%20fitzgerald"

response = requests.get(url)

data = response.json()

with open("author2.json", "w") as json_file:
    json.dump(data, json_file, indent=4)