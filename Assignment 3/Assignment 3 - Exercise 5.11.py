# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:39:38 2020

@author: mstub
"""


#Problem 5.11

string = list(str(input('Enter string: '))) #input string

def summarize_letters(x):
    string2 = [item.lower() for item in x]
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in alphabet:
        print(f'{i}: {string2.count(i)}')
    alphacount = 0
    for item in string2:
        if string2.count(item) > 0:
            alphacount = alphacount + 1
        
    if alphacount == 26:
        print('Your string contains all the letters of the alphabet')
    else:
        print('There are missing letters')

summarize_letters(string)
