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

like = '👍'
dislike ='👎'

while True:
    updates = getUpdates()
    text = getUpdates()[-1]['message']['text']
    if text == like:
        print(1)
    
    elif text == dislike:
        print(0)


pprint(updates)    
    