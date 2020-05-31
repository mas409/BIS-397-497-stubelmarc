# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:56:44 2020

@author: mstub
"""


#Problem 3.1

# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
student = 0

# process 10 students
while student <= 9:
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    student = student + 1

    if result == 1:
        passes = passes + 1
    elif result == 2:
        continue
    else:
        print('Invalid entry.')
        student = student - 1

# termination phase
print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')