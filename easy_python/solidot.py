import urllib2
import csv
import os
from BeautifulSoup import BeautifulSoup

def get_solidot():
    url = "http://www.solidot.org"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()

field_order = ['date', 'context']

fields = {'title' : 'Title',
          'context' : 'Context'}

def find_quota_section(html):
    soup = BeautifulSoup(html)
    quote = soup.findAll('div',attrs={'class': 'p_mainnew'})
    return quote

if __name__ == '__main__':
    html = get_solidot()
    print find_quota_section(html)

