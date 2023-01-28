import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html; charset=utf-8'
    }
    try:
        response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1,target2),headers=headers)
        content = BeautifulSoup(response.content,'html.parser')
        containers = content.find('span',{'id':'last_last'})
        print(containers.text)
    except requests.exceptions.RequestException as e:
        print(e)

get_exchange_rate('usd','krw')