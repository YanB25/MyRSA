from config import *
from random import *
from millerRabinPrimeTest import * 
bit = 70
Min = 2**(bit - 1)
Max = 2**bit - 1
for i in range(10):
    num = randint(Min, Max)
    while primeTest(num) == False:
        num = randint(Min, Max)
    print(num)
#    print(str(primeTest(11)))
