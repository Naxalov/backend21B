import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 
# AgACAgQAAxkDAAOFYB_Uagy6IexogVEu2O-7qo4WxfUAAi2pMRu_5eRRVFC6sJAXyezMcqgbAAQBAAMCAANtAAOqfwACHgQ
def sendPhoto(idx):
    url = f'https://api.telegram.org/bot{token}/sendPhoto'
    photo = open('logo.jpeg','rb')
    payload = {
    'chat_id':idx,
    # 'photo': 'AgACAgQAAxkDAAOFYB_Uagy6IexogVEu2O-7qo4WxfUAAi2pMRu_5eRRVFC6sJAXyezMcqgbAAQBAAMCAANtAAOqfwACHgQ',
    'caption':'TITLE'
    }
    r = requests.post(url,params=payload,files={'photo':photo})
    return r.json()


ids= 86775091
pprint(sendPhoto(ids))

    