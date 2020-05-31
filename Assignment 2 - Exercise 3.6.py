# -*- coding: utf-8 -*-
"""
Created on Wed May 27 21:15:40 2020

@author: mstub
"""


#Problem 3.6
problem = 1

input('What is your problem?: ')
while problem == 1:
    problem = input('Have you had this problem before? (yes or no): ')
    if problem == 'yes':
        print('Well, you have it again.')
    elif problem == 'no':
        print('Well, you have it now.')
    else:
        problem = 1
        print("I didn't understand that...")

#This conversation would not convince the user because there are only 2 outcomes.