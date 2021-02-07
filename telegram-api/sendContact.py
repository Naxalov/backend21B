import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 

def sendContact(idx,number,name):
    url = f'https://api.telegram.org/bot{token}/sendContact'
    payload = {
    'chat_id':idx,
    'phone_number':number,
    'first_name':name
    }
    r = requests.post(url,params=payload)
    return r.json()


ids= 86775091
pprint(sendContact(ids,'123456','User name'))

    