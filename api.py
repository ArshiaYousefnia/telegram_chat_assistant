import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_btc_price():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    api_key = os.getenv("CRYPTO_API_TOKEN")

    headers = {
        'Accept': 'text/plain',
        'X-CoinAPI-Key': api_key
    }

    response_dict = requests.get(url, headers=headers).json()

    return (
        f"BTC USD price:\n"
        f"{int(response_dict.get("rate", "?") * 100) / 100 }\n"
        f"time:\n"
        f"{response_dict.get('time', "?")}"
    )