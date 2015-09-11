#!/usr/bin/env python3

import requests
import sys
import time

def get_page(page_num):
    price_data = ''
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(page_num))
    if req.status_code == 200:
        price_data += req.text
    else:
        price_data += "API error"
    return price_data

def get_first_N(first_N, show=False):
    price_data = ''
    k = 1 
    if show: print(" ... fetching first "+str(first_N))
    while k <= first_N:                                                                               
        price_data +='\n' + get_page(k)
        if show: print(" ... getting page " + str(k))
        k+=1
    return price_data

# slightly better than get_first_N()?
# right now page 149 happens to be the end
def get_range(low_index=1, high_index=149, show=False):
    price_data = ''
    k = low_index
    if show: print("... fetching pages "+str(low_index)+" through "+str(high_index+" ..."))
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
        if show: print("... getting page " + str(page_num))
        page_num += 1
        if new_page == "":
            break
    return price_data

def parse_data(price_data, show=False):
    formatted = price_data.replace(',','\n').split('\n')
    prices = formatted[::2]
    timestamps = formatted[1::2]
    vectors = [timestamps, prices]
    if show:
        print(vectors)
    return vectors 

def prices(price_data, index=None, show=False):
    if index is None:
        if show: 
            print(" ... returning "+str(len(parse_data(price_data)[0]))+" prices in specified range...")
            time.sleep(2)
        return parse_data(price_data)[0]
    else:
        if show:
            print(" ... returning the price of index "+str(index))
        return parse_data(price_data)[0][int(index)]

def timestamps(price_data, index=None, show=False):
    if index is None:
        if show:
            print(" ... returning "+str(len(parse_data(price_data)[0]))+" timestamps in specified range ...")
            time.sleep(2)
        return parse_data(price_data)[1]
    else:
        if show:
            print(" ... returning the timestamp with index "+str(index))
        return parse_data(price_data)[1][int(index)]

if __name__ == '__main__':
    sys.stdout.write(get_all(show=True))        
  
