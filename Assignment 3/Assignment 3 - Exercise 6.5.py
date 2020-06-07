# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:48:58 2020

@author: mstub
"""


#Problem 6.5

from collections import Counter

text = input('Input string: ')

text_lower = text.lower()

counter = Counter(text_lower.split())
unique_words = len(counter)

word_count = 0
duplicates = 0
dup_tot = 0

print('The following words were duplicated:')
for word, count in sorted(counter.items()):
    word_count = word_count + count
    if count > 1:
        print(word)
        duplicates = duplicates + count
        dup_tot = dup_tot + 1

print(f'{dup_tot} words are duplicated in the sentence a total of {duplicates} times')


