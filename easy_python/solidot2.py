import urllib2
#import requests
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

#html ="""
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#<p class="story">...</p>
#"""

def find_quota_section(html):
    soup = BeautifulSoup(html)
    print soup.title.string

    print type(soup.findAll('div' ,{'class' : 'bg_htit'}))

#    print type(soup.findAll('div',attrs={'class': 'p_mainnew'}))
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
    find_quota_section(html)

