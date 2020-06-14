# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:44:44 2020

@author: mstub
"""


#Problem 7.20

import numpy as np
import random
import pandas as pd

x = 1


list_list = []
array_list = []

while x <= 1_000_000:
    list_t = %timeit -o list_time = [random.randrange(1, 7) for i in range(0, x)]
    list_list += [str(list_t.average)]
    array_t = %timeit -o array_time = np.random.randint(1, 7, x)
    array_list += [str(array_t.average)]
    
    x = x * 10

times_dict = {'List Average Execution Time': list_list, 
              'Array Average Execution Time': array_list} 

time_df = pd.DataFrame(times_dict)
time_df.index = ['1', '10', '100', '1,000', '10,000', '100,000', '1,000,000']
print(time_df)
