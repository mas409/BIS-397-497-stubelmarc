# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:46:31 2020

@author: mstub
"""

#Problem 2.12
x10 = 1000 * 1.07 ** 10
x20 = 1000 * 1.07 ** 20
x30 = 1000 * 1.07 ** 30

print("""With an interest rate of 7%, a 1000 USD investment would be worth:
${0:.2f} after 10 years; 
${1:.2f} after 20 years; 
${2:.2f} after 30 years.""".format(x10, x20, x30))
