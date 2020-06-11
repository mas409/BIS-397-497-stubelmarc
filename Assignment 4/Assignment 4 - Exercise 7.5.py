# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 21:12:54 2020

@author: mstub
"""


#Problem 7.5

import numpy as np

array7_5 = np.array([2 ** x for x in range(0, 6)]).reshape(2, 3)

print("Original Array:")
print(array7_5)
print()

#flatten
flattened = array7_5.flatten()

print("Flattened Array:")
print(flattened)
print()
print("Original Array:")
print(array7_5)
print()

#ravel
raveled = array7_5.ravel()

print("Raveled Array:")
print(raveled)
print()
print("Original Array:")
print(array7_5)