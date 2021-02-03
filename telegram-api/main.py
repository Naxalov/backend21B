# 
import requests
import json
from pprint import pprint
token = '1602686596:AAFiy3eteVMwvKw8RT-PU8xgZLlzHqemCK0'
url = f'https://api.telegram.org/bot{token}/getMe'
r = requests.get(url)
user = r.json()
pprint(user)