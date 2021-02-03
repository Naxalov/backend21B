import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']
print(r.url)
# 86775091
# ids = 
for update in updates:
    message = update['message']
    user = message['from']
    user_id = user['id']
    first = user.get('first_name','')
    last = user.get('last_name','')
    print(user_id,end=',')
pprint(updates)    
