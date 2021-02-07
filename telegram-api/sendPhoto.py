import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 

def sendPhoto(idx):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    payload = {
    'chat_id':idx,
    'photo': 'https://random.dog/a1eba572-e557-474b-a023-e48ead3c2786.jpeg'
    }
    r = requests.get(url,params=payload)
    return r.json()


ids= 86775091


    