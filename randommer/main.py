import requests

h = {'X-Api-Key':'a45a594e67814c30883787b95fec5af1'}
url = 'https://randommer.io/api/Card'
payload = {
    'type':'Visa'
}
r = requests.get(url,params=payload,  headers=h)
print(r.url)
print(r.json())