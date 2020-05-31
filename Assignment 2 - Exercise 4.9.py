# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:30:48 2020

@author: mstub
"""


#Problem 4.9

def fahrenheit(c):
    """Convert the Fahrenheit equivalent of a Celsius temperature"""
    f = (9 / 5) * c + 32
    return f

temp = 0

print(f'{"Celsius":>7}{"Fahrenheit":>12}')

for temp in range(101):
    print(f'{temp:>7}{round(fahrenheit(temp),1):>12}') 
    