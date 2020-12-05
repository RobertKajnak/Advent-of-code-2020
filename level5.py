# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:00:01 2020

@author: Hesiris
"""
import numpy as np

ids = []
plane = np.zeros((128,8))
S = 0
with open('input-5-1.txt', 'r') as f:
    for l in f:
        h = 8
        w = 128
        col = 0
        row = 0
        for c in l:
            if c == 'L':
                h = col + int((h-col) /2)
            elif c=='R':
                col = col + int((h-col)/2)
            elif c=='B':
                row += int((w-row)/2)
            elif c == 'F':
                w = row + int((w-row)/2)
        #print(col,h,';',row,w)
        code=  row*8+col
        #print(code, row, col)
        S+=1
        plane[row,col] = 1
        ids.append(code)
            
        

print(max(ids))


for i in range(15,plane.shape[0]-15):
    for j in range(plane.shape[1]):
        if plane[i,j]==0:
            print(i,j)