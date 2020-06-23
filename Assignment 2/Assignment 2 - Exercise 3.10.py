# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:21:42 2020

@author: mstub
"""


#Problem 3.10

n = 1

while n <= 30:
    x = 1000 * 1.07 ** n
    print(f'Your investment will be worth ${x:.2f} after {n} years.')
    n = n + 1