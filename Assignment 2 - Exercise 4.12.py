# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:50:10 2020

@author: mstub
"""


#Problem 4.12

import random

t = 1
h = 1

def tortoise(t):
    plod = random.randrange(1, 11)
    
    if 1 >= plod and plod <= 5: #fast plod
        t = t + 3
    elif plod == 6 or plod == 7: #slip
        t = t - 6
    else:                       #slow plod
        t = t + 1
        
    if t < 1:
        t = 1
    if t > 70:
        t = 70
    
    return t

def hare(h):
    hop = random.randrange(1, 11)
    
    if hop == 3 or hop == 4: #big hop
        h = h + 9
    elif hop == 5: #big slip
        h = h - 12
    elif 6 <= hop <= 8: #small hop
        h = h + 1
    elif hop == 9 or hop == 10: #small slip
        h = h - 2
    else: #sleep
        h = h
    
    if h < 1:
        h = 1
    if h >70:
        h = 70
        
    return h

#begin the race
print("BANG !!!!!")
print("AND THEY'RE OF !!!!!")

while t < 70 and h < 70:
    t = tortoise(t)
    h = hare(h)
    
    if t == h:
        print("OUCH!!!")
    elif t > h:
        counter = 1
        while counter < h:
            print(" ", end="")
            counter = counter + 1
        print("H", end="")
        while counter < t:
            print(" ", end="")
            counter = counter + 1
        print("T")
    else:
        counter = 1
        while counter < t:
            print(" ", end="")
            counter = counter + 1
        print("T", end="")
        while counter < h:
            print(" ", end="")
            counter = counter + 1
        print("H")

if t == 70 and h == 70:
    print("It's a tie...")
elif t == 70:
    print("TORTOISE WINS!!! YAY!!!")
else:
    print("Hare wins... Yuch...")