
import requests

url = 'https://randomuser.me/api/'

payload = {'results':2,'gender':'male'}

r = requests.get(url,payload)
print(r.status_code)
print(r.url)
# data = r.json()['results']
# for i in data:
#     print(i['name'],i['nat'])