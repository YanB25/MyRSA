from math import *
unit =  3/4
confidence = 0.99
TEST_TIMES = ceil(log(1 - confidence, 2) / log(unit, 2))
