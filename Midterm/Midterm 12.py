# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:56:23 2020

@author: mstub
"""


#Midterm Question 12

# Write me a script that creates a function called descriptive, which, 
# when passed a list of numbers, will return the mean, median, 
# sample standard deviation, and population standard deviation, 
# along with appropriate titles.

import random

numbers = []

def descriptive(x):
    """Returns descriptive statistics of a list of numbers"""
    import statistics as stat
    mean = stat.mean(x)
    median = stat.median(x)
    stdev = stat.stdev(x)
    pstdev = stat.pstdev(x)
    
    print(f'Mean: {mean}')
    print(f'Median: {median}')
    print(f'Sample Standard Deviation: {stdev:.2f}')
    print(f'Population Standard Deviation: {pstdev:.2f}')

# Put your function in a script and also have the script call the function on
# a set of 10 random numbers to show me that it works.

for item in range(0, 10):
    numbers += [random.randrange(0, 100)]
    
descriptive(numbers)
    
    