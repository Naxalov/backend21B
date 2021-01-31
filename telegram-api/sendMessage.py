import requests
import json
from pprint import pprint

def sendMsg(idx):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
    'chat_id':idx,
    'text':'Hi!!'
    }
    r = requests.get(url,params=payload)

token = '1602686596:AAFiy3eteVMwvKw8RT-PU8xgZLlzHqemCK0'

ids= [86775091]

# 86775091
for idx in ids:
    sendMsg(idx)

    