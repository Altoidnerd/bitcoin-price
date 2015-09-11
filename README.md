# bitcoin-data
get bitcoin data

    >>> from fast_dump_v21 import *
    >>> parse_data(get_page(1))[0]

returns prices for page 1.

    >>> parse_data(get_page(1))[1]

returns timestamps associated with the previous output

    >>> get_page(1)

returns all the data from page 1.

You can almost always turn on optional debug statements

    >>> get_first_N(3, show=True)
    ... fetching first 3

