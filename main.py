import requests
import os

# "apikey": "3TVA2WYarSx30gtHlNsUF5umTSABZ6Pz"


url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=1"
# VAL_KEY = os.getenv('VAL_KEY')
VAL_KEY = '3TVA2WYarSx30gtHlNsUF5umTSABZ6Pz'
payload = {}
headers = {'apikey': VAL_KEY}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(status_code)
print(result)
