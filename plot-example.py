#!/usr/bin/env python3

from fast_dump_v22 import *
import matplotlib.pyplot as plt
import sys

data = get_first_N(50)

price = prices(data)
bins = list(range(0, len(price)))

plt.plot(bins, price)
plt.show()


