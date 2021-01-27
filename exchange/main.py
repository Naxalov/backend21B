import requests
from pprint import pprint
url = 'https://api.exchangeratesapi.io/latest?base=USD'



r = requests.get(url)
print(r.url)
pprint(r.json())