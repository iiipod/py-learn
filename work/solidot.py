#coding=utf-8
import requests
import re
from bs4 import BeautifulSoup

res = requests.get('http://solidot.org')
#print res.text

soup = BeautifulSoup(res.text)

times = len(soup.findAll('div', attrs={"class": "bg_htit"}))

for i in range(times):
    m =  soup.findAll('div', attrs={"class": "bg_htit"})[i]
    print m.findAll(href=re.compile('story\?sid'))[0].text + ":"
    print soup.findAll('div', attrs={"class": "p_mainnew"})[i].text.strip() + "\n"

