#!/usr/bin/env python3

from price_dump import *
import matplotlib.pyplot as plt

data = get_first_N(10)

price = prices(data)
bins = range(0, len(price))

plt.plot(bins, price[::-1])
plt.show()


