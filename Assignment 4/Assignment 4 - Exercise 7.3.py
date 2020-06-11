# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 20:54:31 2020

@author: mstub
"""


#Problem 7.3

import numpy as np

# 3x3 array, even numbers 2-18
array_1 = np.arange(2, 20, 2).reshape(3, 3)
print("Array 1:")
print(array_1)
print()

# 3x3 array, numbers 9 down to 1 
array_2 = np.arange(9, 0, -1).reshape(3,3)
print("Array 2:")
print(array_2)
print()

# mutliple the arrays
array_product = array_1 * array_2
print("Product of Array 1 and Array 2:")
print(array_product)