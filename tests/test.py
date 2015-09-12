#!/usr/bin/env python3

from fast_dump_v22 import *
import random

t_index1k = random.randint(1, 999)
t_index2k = random.randint(1, 1999)

def timestamps_test_1():
    data = get_page(1)+get_page(2)
    a = timestamps(data)[t_index2k]
    b = timestamps(data, index=t_index2k)
    if not(a == b): 
        result = "FAIL"
    else:
        result = "PASS"
    print("timestamp test 1: ", result)

def timestamps_test_2():
    data = get_page(1)
    a = timestamps(data)[t_index1k]
    b = timestamps(data, index=t_index1k)
    if not(a == b):
        result = "FAIL"
    else:
        result = "PASS"
    print("timestamp test 2: ", result)

def timestamps_test_3():
    data = get_first_N(2)
    a = timestamps(data, index=t_index2k)
    b = timestamps(data)[t_index2k]
    if not(a == b):
        result = "FAIL"
    else:
        result = "PASS"
    print("timestampt test 3: ", result)

def prices_test_1():
    data = get_first_N(2)
    a = prices(data, index=t_index2k)
    b = prices(data)[t_index2k]
    if not(a == b):
        result = "FAIL"
    else:
        result = "PASS"
    print("prices test 1: ", result)
    
def prices_test_2():
    randpage = random.randint(1,145)
    data = get_page(randpage)
    a = prices(data)
    b =  parse(data)[0]
    if not(a == b):
        result = "FAIL"
    else:
        result = "PASS"
    print("prices test 2: ", result)

 # TODO - bedtime now
   # def test_parse(self):
    #    self.assertEqual(parse(get_page(1)+get_page(2))[0], parse(get_first_N(2))[0])
     #   self.assertEqual(parse(get_page(1)+get_page(2)+get_page(3))[0], prices(get_first_N(3)))
      #  self.assertEqual(parse(get_page(2)+get_page(3)[0], prices(get_range(2,3))))
       # self.assertEqual(parse(get_first_N(6))[0] == prices(get_range(1,6)))


def main():                
    timestamps_test_1()     
    timestamps_test_2()     
    timestamps_test_3()
    prices_test_1()
    prices_test_2()

if __name__ == '__main__':                                                                  
    main() 


