import json
import requests

key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
data = requests.get(key)
data = data.json()
print(f"{data['symbol']} price is {data['price']}")
