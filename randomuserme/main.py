
import requests

url = 'https://randomuser.me/api/'

payload = {
    'results':4,
    'gender':'male',
    'nat':'US'
    }

r = requests.get(url,payload)

data = r.json()['results']
for i in data:
    print(i['name'],i['nat'])