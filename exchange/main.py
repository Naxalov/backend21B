# import requests
# from pprint import pprint
# url = 'https://api.exchangeratesapi.io/latest'

# payload = {
#     'base':'USD',
#     'symbols':['RUB','KRW']
# }

# r = requests.get(url=url,params=payload)
# print(r.url)
# pprint(r.json())


def sum1(a,b=0):
    return a+b

print(sum1(4,b=5))