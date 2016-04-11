import urllib2
import requests
import csv
import os
import re
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
    title = soup.findAll('div', attrs={'class': 'bg_htit'})


    for line in title:
        pattern = re.compile('[a-zA-Z]')
        title_line = pattern.findall('>.+<', line)
        print title_line
#    context = soup.findAll('div',attrs={'class': 'p_mainnew'})
#    print context

def write_csv():
    file_name = "solidot.csv"
    if os.access(file_name, os.F_OK):
        file_mode = 'ab'
    else:
        file_mode = 'wb'

    csv_writer = csv.reader(
            open(file_name, file_mode),
            fieldnames = field_order)

    if file_mode == 'wb':
        csv_writer.writer(fields)
    csv_writer.writer(field_order)

if __name__ == '__main__':
    html = get_solidot()
    print find_quota_section(html)

