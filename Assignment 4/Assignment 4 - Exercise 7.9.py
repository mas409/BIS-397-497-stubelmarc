# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:19:18 2020

@author: mstub
"""


#Problem 7.9

import numpy as np

# create 3x5 array with numbers 1-15
array7_9 = np.arange(1, 16).reshape(3, 5)
print(array7_9)
print()

# a) select row 2
print("a)")
print(array7_9[2])
print()

# b) select column 4
print("b)")
print(array7_9[:, 4])
print()

# c) select rows 0 and 1
print("c)")
print(array7_9[0:2])
print()

# d) select columns 2-4
print("d)")
print(array7_9[:, 2:5])
print()

# e) select element in row 1 column 4
print("e)")
print(array7_9[1, 4])
print()

# f) select elements from row 1 and 2 that are in columns 0, 2, and 4
print("f)")
print(array7_9[1:3, [0, 2, 4]])
