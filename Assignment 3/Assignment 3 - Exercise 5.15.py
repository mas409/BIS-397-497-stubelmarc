# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:41:15 2020

@author: mstub
"""


#Problem 5.15

from operator import itemgetter

hardware = [(83, 'Electric Sander', 7, 57.98), (24, 'Power Saw', 18, 99.99),
            (7, 'Sledge Hammer', 11, 21.50), (77, 'Hammer', 76, 11.99),
            (39, 'Jig Saw', 3, 79.50)]

# a) sort by part description
hardware_a = sorted(hardware, key=itemgetter(1))

for row in hardware_a:
    print(f'{row[0]:<3} {row[1]:<16} {row[2]:<3} {row[3]:<5}')
print()

# b) sort by price
hardware_b = sorted(hardware, key=itemgetter(3))

for row in hardware_b:
    print(f'{row[0]:<3} {row[1]:<16} {row[2]:<3} {row[3]:<5}')
print()

# c) map to tuples with part description & quantity, sort by quantity
hardware_c = []

for row in hardware:
    tup = (row[1], row[2]) 
    hardware_c += [tup]

hardware_c2 = sorted(hardware_c, key=itemgetter(1))

for row in hardware_c2:
    print(f'{row[0]:<16} {row[1]:<3}')
print()

# d) map to tuples with description and value, sort by value
hardware_d = []

for row in hardware:
    tup = (row[1], row[2] * row[3]) 
    hardware_d += [tup]

hardware_d2 = sorted(hardware_d, key=itemgetter(1))

for row in hardware_d2:
    print(f'{row[0]:<16} {round(row[1], 2):>8}')
print()

# e) Filter results of d to invoices between $200 and $500
hardware_e = []

for row in hardware_d2:
    if row[1] >= 200 and row[1] <= 500:
        tup = (row[0], row[1]) 
        hardware_e += [tup]

for row in hardware_e:
    print(f'{row[0]:<16} {round(row[1], 2):>8}')
print()

# f) calculate the total of all the invoices
total = 0

for row in hardware_d:
    total += row[1]
print(f'The total of all the invoices is ${total}')

