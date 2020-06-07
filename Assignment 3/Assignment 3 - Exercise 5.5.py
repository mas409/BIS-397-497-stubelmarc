# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:38:11 2020

@author: mstub
"""


#Problem 5.5

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#a) the first half of the string using starting and ending indices
print(alphabet[0:13])

#b) the first half of the string using only the ending index
print(alphabet[:13])

#c) the second half of the string using starting and ending indices
print(alphabet[14:26])

#d) the second half of the string using only the starting index
print(alphabet[14:])

#e) every second letter in the string starting with a
print(alphabet[::2])

#f) entire string in reverse
print(alphabet[::-1])

#g) every third letter in the string in reverse starting with z
print(alphabet[::-3])
