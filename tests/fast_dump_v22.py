#!/usr/bin/env python3

import requests
import sys
import time

def get_page(page_num):
    price_data = ''
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(page_num))
    if req.status_code == 200:
        price_data += req.text+'\n'
    else:
        price_data += "API error"
    return price_data

def get_first_N(first_N, show=False):
    price_data = get_page(1)
    k = 2
    if show: print(" ... fetching first "+str(first_N))
    while k <= first_N:                                                                               
        price_data += get_page(k)
        if show: print(" ... getting page " + str(k))
        k+=1
    return price_data

# slightly better than get_first_N()?
# right now page 149 happens to be the end
def get_range(low_index=1, high_index=149, show=False):
    price_data = get_page(low_index)
    k = low_index + 1
    if show: print("... fetching pages "+str(low_index)+" through "+str(high_index+" ..."))
    while k <= high_index:
        price_data += get_page(k)
        if show == True: print("... getting page " + str(k))
        k+=1
    return price_data

def get_all(show=False):
    price_data = get_page(1)
    page_num = 2
    while True:
        new_page = get_page(page_num)
        price_data +=  new_page
        if show: print("... getting page " + str(page_num))
        page_num += 1
        if new_page == "\n":
            break
    return price_data

def parse(price_data, show=False):
    formatted = price_data.replace(',','\n').split('\n')
    timestamps = formatted[::2]
    del timestamps[-1]
    prices = formatted[1::2]
    vectors = [prices, timestamps]
    if show:
        print(vectors)
    return vectors 

def prices(price_data, index=None, show=False):
    if index is None:
        if show: 
            print(" ... returning "+str(len(parse(price_data)[0]))+" prices in specified range...")
            time.sleep(2)
        return parse(price_data)[0]
    else:
        if show:
            print(" ... returning the price of index "+str(index))
        return parse(price_data)[0][int(index)]

def timestamps(price_data, index=None, show=False):
    if index is None:
        if show:
            print(" ... returning "+str(len(parse(price_data)[0]))+" timestamps in specified range ...")
            time.sleep(2)
        return parse(price_data)[1]
    else:
        if show:
            print(" ... returning the timestamp with index "+str(index))
        return parse(price_data)[1][int(index)]

if __name__ == '__main__':
    sys.stdout.write(get_all(show=True))        
  
