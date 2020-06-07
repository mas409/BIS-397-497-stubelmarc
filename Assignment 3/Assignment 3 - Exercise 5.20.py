# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:46:07 2020

@author: mstub
"""


#Problem 5.20


def display_table(x):
    """Display the contents of a two-dimensional list in tabular form"""
    rownum = 0
    print(f'{"":>10}', end='')
    for item in headings:
        print(f'{item:>10}', end='')
    print()
    for row in x:
        print(f'{indices[rownum]:>10}', end='')
        for item in row:
            print(f'{item:>10}', end='') 
        print()
        rownum = rownum + 1

headings = ['column1', 'column2', 'column3']
indices = ['row1', 'row2', 'row3']
table = [[77, 68, 86], [96, 87, 89], [70, 90, 86]]

display_table(table)



