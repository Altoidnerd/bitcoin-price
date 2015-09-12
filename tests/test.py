#!/usr/bin/env python3

from fast_dump_v22 import *
import unittest 

class TestParser(unittest.TestCase):

    def test_stamps(self):
      self.assertEqual(timestamps(get_page(1)+get_page(2))[1166], timestamps(get_range(1,2), index=1166))
      self.assertEqual(timestamps(get_page(1))[466], timestamps(get_page(1), index=466))
      self.AssertEqual(timestamps(get_first_N(2), index=1776), timestamps(get_first_N(2))[1776])

    def test_prices(self):
      self.assertEqual(prices(get_first_N(2), index=1776), prices(get_first_N(2))[1776])
      self.assertEqual(prices(get_page(2)), parse(get_page(2))[0])

    def test_parse(self):
      self.assertEqual(parse(get_page(1)+get_page(2))[0], parse(get_first_N(2))[0])
      self.assertEqual(parse(get_page(1)+get_page(2)+get_page(3))[0], prices(get_first_N(3)))
      self.assertEqual(parse(get_page(2)+get_page(3)[0], prices(get_range(2,3))))
      self.assertEqual(parse(get_first_N(11))[0] == prices(get_range(1,11)))

if __name__=='__main__':
    unittest.main()




