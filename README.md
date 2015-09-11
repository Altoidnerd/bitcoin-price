Copyright (c) 2015 Altoidnerd
http://altoidnerd.com

![plot.png](https://raw.githubusercontent.com/Altoidnerd/bitcoin-price/master/plot.png "plot-example.py in action - matplotlib required")
http://altoidnerd.com/2015/09/11/bitcoin-data-manipulaton-and-plotting-in-python/

# bitcoin-data manipulaton and plotting

Get bitcoin price data from the coinbase API and parse it into an easily manipulated form.

    >>> from fast_dump_v22 import *
    >>> get_page(1)

Will return all the data on page 1 of coinbase's bitcoin price API (this is the latest data).

You can almost always turn on optional debug statements

    >>> get_first_N(3, show=True)
    ... fetching first 3

You can get all the price data that coinbase has

    >>> get_all(show=True)
    ... getting page 1
    ... getting page 2
    ... getting page 3
    ... getting page 4
    ... getting page 5
    ... getting page 6
    ... getting page 7
    ... getting page 8
    ... getting page 9
    ... etc ...

All the 'get_*' functions return a price_data string, which is interlaced timespams and prices littered with newlines and commas.  You can print them to see what is going on more clearly:

    >>> print(get_page(1))
    2015-09-11T06:44:04-05:00,241.14
    2015-09-11T06:34:04-05:00,240.8
    2015-09-11T06:24:04-05:00,240.75
    2015-09-11T06:14:05-05:00,240.68
    2015-09-11T06:04:04-05:00,240.83
    2015-09-11T05:54:05-05:00,240.92
    2015-09-11T05:44:04-05:00,240.64
    2015-09-11T04:34:04-05:00,241.27
    2015-09-11T04:24:04-05:00,240.73
    ...
    
    
Turn on the optional show switch for printing large vectors

    >>> prices(get_page(11), show=True)
    ... returning 11000 prices in specified range ...
    ['239.9',
    '239.9',
    '239.4',
    '239.77',
    '239.33',
    '239.99',
    '239.81',
    '240.28',
    '240.4',
You can use prices(data)[k] and timestamps()[j] to return the kth price in data, or the jth timestamp in data.

    >>> data = get_page(1)
    >>> prices(data)[4]
    '241.2'
    >>> prices(data, index=4)
    '241.2' 

are two equivalent ways of returning only the 4th price in the requested range (in this case, page 1).  This also works for timestamps.  

    >>> timestamps(get_page(1)+get_page(2))[1166] == timestamps(get_first_N(2), index=1166)
    True

This shows the expressiveness of this module. In general:

    >>> prices(get_page(2)) == parse(get_page(2))[0]
    True

prices() and timestamps() are just functions that return a parsed() object having a specific index, or indices. 

    >>> parse(get_page(1)+get_page(2)+get_page(3))[0] == prices(get_first_N(3))  
    True
    >>> parse(get_page(2)+get_page(3))[0] == prices(get_range(2,3))
    True
    
The parse() function is there to manually control the outputs instead of just getting prices, or timestamps

    >>> x = parse(get_page(1))
    >>> x[0][0]
    '241.2'
    >>> x[0][1]
    '241.14'
    >>> x[1][1]
    '2015-09-11T04:34:04-07:00'

As you can see, parse(price_data)[0][k] returns the kth price in the list.  Indices [1][k] return the kth timestamp.  

The parse() function takes care of some weird edge cases:

    >>> get_first_N(3) == get_page(1)+get_page(2)+get_page(3)
    False
    >>> parse(get_first_N(3)) == parse(get_page(1)+get_page(2)+get_page(3))
    True
    >>> x = get_page(1)
    >>> y = get_range(2,7)
    >>> prices(get_first_N(7)) == prices(x+y)
    True
    
    
In general,

    OPERATOR( get_page(1) + get_page(2) + ... + get_page(k) ) == OPERATOR(get_first_N(k))

where operator is parsed(), prices(), or timestamps().  We also know

prices() can obviously display and return ranges of values.  When returning large vectors, you can verify their length by setting show=True.  The "show" parameter is optional for all get\_\* functions and provides some information about the operation being performed.

    >>> print( prices(get_first_N(11), show=True) )
    ... returning 11000 prices in specified range...

since each page is a thousand pairs of values (timestamp, price).

    >>> len(prices(get_page(2))
    1000
    >>> prices(get_page(2))  # returns a long list
    ['230.11',
     '229.64',
     '230.04',
     '229.71',
     '229.69',
     '229.74',
     '229.92',
     '229.43',
     '229.43',
     '229.41',
    ...


* fast_dump_v1* are older versions that are somewhat different.  They are designed to store the fetched data in the .data directory.  This in v2*, this was abandoned in favor of stdout redirection.



// 2015 altodinerd.com

