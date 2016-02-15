# coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import csv
import os
import time

def get_solidot_html():
    opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
        )
    opener.addheaders = [
        ('User-agent',
         "Mozilla/4.0 (compatible; MSIE 7.0; "
         "Windows NT 5.1; .NET CLR 2.0.50727; "
         ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]
    url = "http://solidot.org"
    response = opener.open(url)
    return ''.join(response.readlines())

def find_quote_section(html):
    soup = BeautifulSoup(html, "html.parser")
    quote = soup.find_all('div', attrs={'class': 'block_m'})
    print quote
    return quote


def parse_stock_html(html):
    quote = find_quote_section(html)
    result = {}

    # 分类
    result['style'] = quote.find('h2',
            attrs={'a': 'solidot'}).contents[0]

    # 标题
    result['title'] = quote.find('h2',
        attrs={'a': 'id'}).contents[1]

    # 内容

    result['contents'] = quote.find('div',
        attrs={'class': 'p_mainnew'}).contents[2]

#    def is_price_change(value):
#        return (value is not None and
#            value.strip().lower()
#                 .startswith('yfi-price-change'))
#    result['change'] = (
#        quote.find(attrs={'id': 'yfs_c10_'})
#             .find(attrs={'class': is_price_change})
#             .string)

    print result
    return result

field_order = ['style', 'title', 'contents']
fields = {'style' : 'Unit',
          'title' : 'Title',
          'contents' : 'Contents'
         }
#def write_row(stock_values):
#    file_name = "solidot-"  + ".csv"
#    if os.access(file_name, os.F_OK):
#        file_mode = 'ab'
#    else:
#        file_mode = 'wb'
#    csv_writer = csv.DictWriter(
#        open(file_name, file_mode),
#        fieldnames=field_order,
#        extrasaction='ignore')
#    if file_mode == 'wb':
#        csv_writer.writerow(fields)
#    csv_writer.writerow(stock_values)

if __name__ == '__main__':
    html = get_solidot_html()
    find_quote_section(html)
#    stock = find_quote_section(html)
#    stock['date'] = time.strftime("%Y-%m-%d %H:%M")
#    write_row(stock)
#    print stock

