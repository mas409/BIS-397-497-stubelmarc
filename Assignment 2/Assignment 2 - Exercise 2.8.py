# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:31:51 2020

@author: mstub
"""



#Problem 2.8
print('number \t square \t cube')
print(0,'\t \t', 0 ** 2, '\t \t \t', 0 ** 3)
print(1,'\t \t', 1 ** 2, '\t \t \t', 1 ** 3)
print(2,'\t \t', 2 ** 2, '\t \t \t', 2 ** 3)
print(3,'\t \t', 3 ** 2, '\t \t \t', 3 ** 3)
print(4,'\t \t', 4 ** 2, '\t \t', 4 ** 3)
print(5,'\t \t', 5 ** 2, '\t \t', 5 ** 3)

#Problem 2.8 - Part 2
print(f'{"number":>6}{"square":>7}{"cube":>7}')
for number in range(6):
    print(f'{number:>6}{number ** 2:>7}{number ** 3:>7}')