import requests
from pprint import pprint
url = 'https://api.exchangeratesapi.io/latest'

payload = {
    'base':'USD',
    'symbols':['RUB','KRW']
}

r = requests.get(url,payload)
print(r.url)
pprint(r.json())