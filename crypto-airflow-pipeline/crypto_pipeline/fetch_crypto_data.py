
import requests
import pandas as pd         

def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd',
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame([
        {'name': 'bitcoin', 'price_usd': data['bitcoin']['usd']},
        {'name': 'ethereum', 'price_usd': data['ethereum']['usd']}
    ])

    df['date'] = pd.Timestamp.now()

    return df