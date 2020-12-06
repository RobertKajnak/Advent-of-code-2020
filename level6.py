# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:00:17 2020

@author: Hesiris
"""


#group = set([chr(c) for c in range(ord('a'),ord('z')+1)])
group = set()
S = 0
with open('input-6-0.txt', 'r') as f:
    for l in f:
        if l == '\n':
            S += len(group)
            print(group)
            group = set()
        else:
            for c in l:
                if c!='\n':
                    group.add(c)
                    
print(S)

#%% Part 2
import string

group = set(string.ascii_lowercase)
S = 0
with open('input-6-1.txt', 'r') as f:
    for l in f:
        if l == '\n':
            S += len(group)
            group = set(string.ascii_lowercase)
        else:
            group = group.intersection(set(l[:-1]))
                    
print(S)