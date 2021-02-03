import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 
def getUpdates():
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    r = requests.get(url)
    data = r.json()
    updates = data['result']
    return updates

# 86775091
update_len = len(getUpdates())
update_len_last = len(getUpdates())


while True:
    update_len_last = len(getUpdates())

    if update_len != update_len_last:
        print(f'len:{update_len} len_last:{update_len_last}')
        update_len = len(getUpdates())