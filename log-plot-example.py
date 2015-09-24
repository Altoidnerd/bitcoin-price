#!/usr/bin/env python3                                                                                                              
 
from price_dump import *
import matplotlib.pyplot as plt
import math
 
data  = get_first_N(15, show=True) 
price = prices(data) 
 
# prices(data) is a list of numeric strings like
# ['241.11', '241.01', ...] so we need to convert the 
# those list entries to floats in order to take the log
 
float_price = map(float, price)
logs        = list(map(math.log10,float_price))
bins        = range(0, len(price))
 
plt.plot(bins, logs[::-1])
plt.show()
