import requests


url = "https://fakestoreapi.com/products"
response = requests.get(url)
products = response.json()

print(products)