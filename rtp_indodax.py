# this script will take some data from Indodax using their official API.
# Indodax is one of the biggest crypto market in Indonesia.

import requests
import json

url = 'https://indodax.com/api/summaries'

results = requests.get(url).json()

print(f"{results['tickers']['btc_idr']['name']}")

# Use currency format for high/low price
HighPrice = int(f"{results['tickers']['btc_idr']['high']}")
HargaTertinggi = '{:,.2f}'.format(HighPrice)

LowPrice = int(f"{results['tickers']['btc_idr']['low']}")
HargaTerendah = '{:,.2f}'.format(LowPrice)

print(f"Harga tertinggi Rp."+HargaTertinggi)
print(f"Harga terendah Rp."+HargaTerendah)
