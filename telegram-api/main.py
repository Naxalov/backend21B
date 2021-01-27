# 
import requests
token = '1602686596:AAFYiu-BmY2WExRhk9tvgW5ZBkAoTaICuQM'
url = f'https://api.telegram.org/bot{token}/getMe'
r = requests.get(url)
print(r.json())