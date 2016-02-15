# coding=utf-8  

import urllib2
import csv
import os
import time
from bs4 import BeautifulSoup

global html
def get_stock_html(ticker_name):
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
    url = "http://finance.yahoo.com/q?s=" + ticker_name
#    url = "http://127.0.0.1:82/index.php?page=robots-txt.php"
    response = opener.open(url)
    html = response.read()

    soup = BeautifulSoup(html)
    quote = soup.find('div',
            attrs={'class': 'yfi_quote_summary'})
    print quote

def parse_stock_html(html, ticker_name):
    find = {}
    tick = ticker_name.lower()
    result['stock_name'] = quote.find('h2').contents[0]

    result['ah_price'] = quote.find('span',
            attrs={'id': 'yfs_l91_' + tick}).string

    result['ah_change'] = (quote.find(
            attrs={'id': 'yfs_z08_' + tick}).contents[1])

    result['last_trade'] = quote.find(
            'span', attrs={'id': 'yfs_l10_' + tick}).string

    def is_price_change(value):
        return (value is not None and value.strip().lower().startswich('yfi-price-change'))

    result['change'] = (quote.find(attrs={'id': 'yfs_c10_' +tick}).find(attrs={'calss': is_price_change}).string)

    return result

####

field_order = ['date', 'last_trade', 'change', 'ah_price', 'ah_change']

fields = {'date' : 'Date',
        'last_trade' : 'Last Trade',
        'change' : 'Change',
        'ah_price' : 'After Hours Price',
        'ah_change' : 'After Hours Change'}

def write_row(ticker_name, stock_values):
    file_name = "stocktracker-" + ticker_name + ".csv"
    if os.access(file_name, os.F_OK):
        file_mode = 'ab'
    else:
        file_mode = 'wb'

    csv_writer = csv.DictWriter(
            open(file_name, file_mode),
            fieldnames = field_order,
            extrasaction = 'ignore')

    if file_mode == 'wb':
        csv_writer.write_row(fields)
    csv_writer.write_row(stock_values)

if __name__ == '__main__':
    quote = get_stock_html('GOOG')
    stock = parse_stock_html(quote)
    stock['date'] = time.strftime("%Y-%m-%d %H:%M")
    write_row('GOOG', stock)
    print stock

