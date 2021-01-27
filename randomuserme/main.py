
import requests

url = 'https://randomuser.me/api/'

payload = {
    'results':15,
    'gender':'male',
    'nat':['GB','US']
    }

r = requests.get(url,payload)
print(r.url)
data = r.json()['results']
for i in data:
    print(i['name'],i['nat'])