import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 

def sendKeyboard(idx):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
    'chat_id':idx,
    'text':'Button',
    'reply_markup':{
        'keyboard':[[{'text':'1'},{'text':'2'}]]
    }
    }
    r = requests.post(url,json=payload)
    return r.json()


ids= 86775091
pprint(sendKeyboard(ids))
# pprint(sendContact(ids,'123456','User name'))




    