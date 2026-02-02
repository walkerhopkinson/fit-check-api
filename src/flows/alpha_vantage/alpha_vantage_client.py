from config import ALPHA_VANTAGE_API_KEY

import requests

import polars as pl

def get_latest_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    return data.get('Global Quote', {})


def get_winners_losers():
    url = f"https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    winners = pl.DataFrame(data['top_gainers'])
    losers = pl.DataFrame(data['top_losers'])
    
    return winners, losers