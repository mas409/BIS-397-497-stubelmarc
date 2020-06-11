# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:52:11 2020

@author: mstub
"""


#Problem 7.14

import numpy as np

array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])
print("array1:")
print(array1)
print("array2:")
print(array2)
print()

# a) vertical stack array1 on top of array2
array3 = np.vstack((array1, array2))
print("a) array 3:")
print(array3)
print()

# b) horizontal stack array2 to the right of array1
array4 = np.hstack((array1, array2))
print("b) array 4:")
print(array4)
print()

# c) vertical stack two copies of array4
array5 = np.vstack((array4, array4))
print("c) array 5:")
print(array5)
print()

# d) horizontal stack two copies of array3
array6 = np.hstack((array3, array3))
print("d) array 6:")
print(array6)
print()