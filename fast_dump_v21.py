#!/usr/bin/env python3

import requests
import sys

def get_page(page_num):
    price_data = ''
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(page_num))
    if req.status_code == 200:
        price_data += req.text
    else:
        price_data += "API error"
    return price_data

# an improvement on get first N?
# right now page 149 happens to be the end
def get_range(low_index=1, high_index=149, show=False):
    price_data = ''
    k = low_index
    if show == True: print("... fetching pages "+str(low_index)+" through "+str(high_index+" ...")
    while k <= high_index:
        price_data +='\n' + get_page(k)
        if show == True: print("... getting page " + str(k))
        k+=1
    return price_data

def get_all(show=False):
    price_data = ''
    page_num = 1
    while True:
        new_page = get_page(page_num)
        price_data += '\n' + new_page
        if show == True: print("... getting page " + str(page_num))
        page_num += 1
        if new_page == "":
            break
    return price_data

def parse_data(price_data, show=False):
    formatted = price_data.replace(',','\n').split('\n')
    prices = formatted[::2]
    timestamps = formatted[1::2]
    vectors = [timestamps, prices]
    if show == True:
        print(vectors)
    return vectors 

        
if __name__ == '__main__':
    sys.stdout.write(get_all(show_page=True))        
  
