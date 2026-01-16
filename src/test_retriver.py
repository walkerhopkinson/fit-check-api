import requests

def fetch_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    products = response.json()

    return products
