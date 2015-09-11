Copyright (c) 2015 Altoidnerd
http://altoidnerd.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# bitcoin-data

Get bitcoin price data from the coinbase API and parse it into an easily manipulated form.

    >>> from fast_dump_v21 import *

returns all the data from page 1.

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

All the 'get\_\*' functions return a price_data string, which is interlaced timespams and prices littered with newlines and commas.  You can print them to see what is going on more clearly:

    >>>> print(get_page(1))
    2015-09-11T06:44:04-05:00,241.14
    2015-09-11T06:34:04-05:00,240.8
    2015-09-11T06:24:04-05:00,240.75
    2015-09-11T06:14:05-05:00,240.68
    2015-09-11T06:04:04-05:00,240.83
    2015-09-11T05:54:05-05:00,240.92
    2015-09-11T05:44:04-05:00,240.64
    2015-09-11T04:34:04-05:00,241.27
    2015-09-11T04:24:04-05:00,240.73

The parse_data() function is there to separate these components. 

    >>> parsed = parse_data(get_page(1))
    >>> x[0][0]
    '241.2'
    >>> x[0][1]
    '241.14'
    >>> x[1][1]
    '2015-09-11T04:34:04-07:00'

As you can see, pase_data(price_data_[0][k] returns the kth price in the list.  Indices [1][k] return the kth timestamp.  

fast_dump_v1* are older versions that are somewhat different.  They are designed to store the fetched data in the .data directory.  This in v2*, this was abandoned in favor of stdout redirection.



// 2015 altodinerd.com

