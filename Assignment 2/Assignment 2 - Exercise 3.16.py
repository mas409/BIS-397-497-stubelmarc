# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:43:09 2020

@author: mstub
"""


#Problem 3.16

counter = 0
number = 0
largest2 = 0
largest1 = 0
largest1 = int(input("Enter number: "))

while counter < 9:
    number = int(input("Enter number: "))
    counter += 1
    
    if number > largest1:
        largest1 = number
    if largest1 > largest2:
        number = largest2
        largest2 = largest1
        largest1 = number

print("The two largest numbers are", largest2, "and", largest1)
