import requests

url = 'https://randomuser.me/api/'
p = {'results':2}
r = requests.get(url)
print(r.url)
# print(r.json())