# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:20:56 2020

@author: Marc Stubel
"""


#Midterm Question 11 - Yahtzee!

import random

#first roll
dice1 = random.randrange(1, 7)
dice2 = random.randrange(1, 7)
dice3 = random.randrange(1, 7)
dice4 = random.randrange(1, 7)
dice5 = random.randrange(1, 7)
choice = 0

print('You rolled: ', dice1, dice2, dice3, dice4, dice5)

#choose dice for second roll
while choice != -99:
    choice = int(input('Which dice would you like to roll again?\n'
                   '(enter dice number 1-5; -99 to re-roll): '))
    if choice == 1:
        dice1 = random.randrange(1, 7)
    elif choice == 2:
        dice2 = random.randrange(1, 7)
    elif choice == 3:
        dice3 = random.randrange(1, 7)
    elif choice == 4:
        dice4 = random.randrange(1, 7)
    elif choice == 5:
        dice5 = random.randrange(1, 7)
    elif choice != -99:
        print('Invalid entry, select again.')

print()
print("You're second roll is: ", dice1, dice2, dice3, dice4, dice5)

choice = 0

#choose dice for third roll
while choice != -99:
    choice = int(input('Last roll.  Which dice would you like to roll again?\n'
                   '(enter dice number 1-5; -99 to re-roll): '))
    if choice == 1:
        dice1 = random.randrange(1, 7)
    elif choice == 2:
        dice2 = random.randrange(1, 7)
    elif choice == 3:
        dice3 = random.randrange(1, 7)
    elif choice == 4:
        dice4 = random.randrange(1, 7)
    elif choice == 5:
        dice5 = random.randrange(1, 7)
    elif choice != -99:
        print('Invalid entry, select again.')

print()
print("You're final roll is: ", dice1, dice2, dice3, dice4, dice5)

if dice1 == dice2 and dice1 == dice3 and dice1 == dice4 and dice1 == dice5:
    print('Yahtzee!')