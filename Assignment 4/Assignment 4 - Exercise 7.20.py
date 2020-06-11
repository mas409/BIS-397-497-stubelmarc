# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:44:44 2020

@author: mstub
"""


#Problem 7.20

import numpy as np
import random

x = 1

while x <= 1_000_000:
    print(f'{x} element list')
    %timeit list_time = [random.randrange(1, 7) for i in range(0, x)]
    print(f'{x} element array')
    %timeit array_time = np.random.randint(1, 7, x)
    
    x = x * 10