# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:50:56 2020

@author: Hesiris
"""
import numpy as np



with open('input-3-1.txt') as f:
    #print(len(f))
    lines = f.readlines()

m = np.zeros((len(lines), len(lines[0])-1))
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c=='#':
            m[i,j] = 1

P=1
for x,y in zip([1,3,5,7,1],[1]*4+[2]):
    
    j = 0
    S = 0
    for i in range(0,len(lines), y):
        if m[i,j] == 1:
            S+=1
        j += x
        if j>=m.shape[1]:
            j -= m.shape[1]
            
    print(S)
    P *= S
    
print(P)