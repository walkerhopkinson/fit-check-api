from config import ALPHA_VANTAGE_API_KEY

import requests

def get_latest_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    latest_price = data['Global Quote']['05. price']
    return latest_price

