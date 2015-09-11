#!/usr/bin/env python3

from fast_dump_v22 import *
 

timestamps(get_page(1)+get_page(2))[1166] == timestamps(get_range(1,2), index=1166)

timestamps(get_page(1))[466] == timestamps(get_page(1), index=466)

timestamps(get_first_N(2), index=1776) == timestamps(get_first_N(2))[1776]

prices(get_first_N(2), index=1776) == prices(get_first_N(2))[1776]

prices(get_page(2)) == parse(get_page(2))[0]

parse(get_page(1)+get_page(2))[0] == parse(get_first_N(2))[0]

parse(get_page(1)+get_page(2)+get_page(3))[0] == prices(get_first_N(3))

parse(get_page(2)+get_page(3)[0] == prices(get_range(2,3))

parse(get_first_N(11))[0] == prices(get_range(1,11)) 



