import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.naver.com')
print(res.text)
print(res.headers)


soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

div = soup.div
print(div)
print(type(div))

#owl > div > div > div:nth-child(2) > a > div > strong