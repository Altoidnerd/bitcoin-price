#!/usr/bin/env python3

import requests


def get_page(page_num):
    page = ''
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(page_num))
    if req.status_code == 200:
        page += '\n' + req.text
    else:
        page += "API error"
    print("... getting page "+str(page_num))
    #if req.content == "":
     #   print("nothing here ... ")
    return page

def get(first_N):
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
        price_data += '\n' + get_page(page_num)
        page_num += 1
        if get_page(page_num) == "":
            break
    return price_data
        
        
  
