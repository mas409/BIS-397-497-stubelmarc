# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:46:07 2020

@author: mstub
"""


#Problem 5.28

import statistics as stat
import numpy as np

survey = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
values, frequencies = np.unique(survey, return_counts=True)

#Display frequency of each rating
print(f'{"Rating":>6}{"Frequency":>10}')
for i in range(0, 5):
    print(f'{values[i]:>6}{frequencies[i]:>10}')

#display minimum, maximum, range, mean, median, mode, variance, std dev
print("Minimum:", min(survey))
print("Maximum:", max(survey))
print("Range:", max(survey) - min(survey)) #range
print("Mean:", stat.mean(survey))
print("Median:", stat.median(survey))
print("Variance", stat.pvariance(survey))
print("Standard Deviation:", stat.pstdev(survey))
