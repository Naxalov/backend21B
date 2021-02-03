import requests
import json
from pprint import pprint
import os

token =os.environ['TOKEN'] 
def sendMsg(idx,text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    payload = {
    'chat_id':idx,
    'text':text,
    'parse_mode':'MarkdownV2'
    }
    r = requests.get(url,params=payload)


# 86775091

link = '[Channel](https://t.me/codeschooluz)'



sendMsg(86775091,'~_*Hello*_ **World**~ '+link)

