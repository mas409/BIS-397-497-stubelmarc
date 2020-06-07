# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:33:50 2020

@author: mstub
"""


#Problem 6.8

#dictionary for numbers 1-19 and tens
words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 
            90: 'Ninety'}

valid = 0
while valid == 0:
    check = float(input('Check value: '))
    
    if check > 999.99:
        print('Check value is too high, enter a value lower than 1000')
    else:
        valid = 1

cents = check % 1
ones = int((check - cents) % 10)
teens = int((check - cents) % 100)
tens = int((check - cents) % 100) - ones
hundreds = int((check - cents) % 1000) - tens - ones

 
if teens < 20 and teens != 0: 
    tenword = words1[teens]
    oneword = ''
elif tens != 0:
    tenword = words1[tens]
    if ones != 0:
        oneword = words1[ones]
    else:
        oneword = ''
else:
    tenword = ''
    if ones != 0:
        oneword = words1[ones]
    else:
        oneword = ''

if hundreds != 0:
    hund = int(hundreds / 100)
    hundword = words1[hund]
    
    print(f'{hundword} Hundred {tenword} {oneword} and '
          f'{round(cents * 100, 2):.0f}/100')
else:
    print(f'{tenword} {oneword} and {round(cents * 100, 2):.0f}/100')    



          

