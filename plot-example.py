#!/usr/bin/env python3

from price_dump import *
import matplotlib.pyplot as plt

data = get_first_N(15, show=True) # keep this number small to start.  Currently there are about 148 pages available.

price = prices(data)
bins = range(0, len(price))

plt.plot(bins, price[::-1])
plt.show()


