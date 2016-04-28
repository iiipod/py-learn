import requests
from bs4 import BeautifulSoup

res = requests.get('http://jiandan.net/ooxx/page-1960')
html = BeautifulSoup(res.text)
for index, each in enumerate(html.select('#comments img')):
    with open('{}.jpg'.format(index), 'wb') as jpg:
        jpg.write(requests.get(each.attrs['src'], stream=True).content)
