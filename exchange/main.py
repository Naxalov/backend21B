import requests

url = 'https://randomuser.me/api/?results=5&gender=male&nat=us,gb'

r = requests.get(url)
data = r.json()['results']
for i in data:
    print(i['name'],i['nat'])
