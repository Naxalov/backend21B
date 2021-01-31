import requests
import json
from pprint import pprint
token = '1602686596:AAFiy3eteVMwvKw8RT-PU8xgZLlzHqemCK0'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']

update = updates[0]
message = update['message']
user = message['from']
print(user)