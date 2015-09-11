#!/usr/bin/env python3

import requests
import sys

def get_page(page_num):
    page = ''
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(page_num))
    if req.status_code == 200:
        page += req.text
    else:
        page += "API error"
    return page

def get_first_N(first_N):
    price_data = ''
    k = 1
    while k <= first_N:
        price_data +='\n' + get_page(k)
        k+=1
    return price_data

def get_all():
    price_data = ''
    page_num = 1
    while True:
        new_page = get_page(page_num)
        price_data += '\n' + new_page
        print("... getting page " + str(page_num))
        page_num += 1
        if new_page == "":
            break
    return price_data
        
if __name__ == '__main__':
    sys.stdout.write(get_all())        
  
