import requests
from config import ALPHA_VANTAGE_API_KEY

BASE_URL = "https://www.alphavantage.co/query"

def get_intraday(symbol="AAPL", interval="5min"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    return response.json()
