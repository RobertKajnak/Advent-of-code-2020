# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:56:21 2020

@author: Hesiris
"""

import numpy as np

with open('input-11-1.txt', 'r') as f:
    lines = f.readlines()
    
M = np.zeros((len(lines),len(lines[0])-1)) #-\n
for x,l in enumerate(lines):
    for y,c in enumerate(l):
        if c =='.':
            M[x,y] = -1
        elif c=='L':
            M[x,y] = 0
            
def get_adjacent(M,x,y):
    return [M[i,j] 
            for i in range(max(0,x-1),min(M.shape[0],x+2)) 
                for j in range(max(0,y-1),min(M.shape[1],y+2))
                    if (i!=x or j!=y)
            ]


def _line(M,x,y,dx,dy):
    i=x+dx;j=y+dy
    while i>=0 and j>=0 and i<M.shape[0] and j<M.shape[1]:
        if M[i,j]==1:
            return 1
        if M[i,j]==0:
            return 0
        i+=dx;j+=dy
    return 0

def get_occupied2(M,x,y):
    
    return sum([_line(M,x,y,i,j) 
        for i in range(-1,2) 
            for j in range(-1,2)
                if (i!=0 or j!=0)
        ])
        
        

def get_occupied(A,x,y):
    return sum(np.array(get_adjacent(A,x,y))==1)

def flip(A,B):
    for x in range(A.shape[0]):
        for y in range(A.shape[1]):
            if A[x,y]==0 and get_occupied2(A,x,y)==0:
                B[x,y] = 1
            elif A[x,y]==1 and get_occupied2(A,x,y)>=5:
                B[x,y] = 0

Mo = M.copy()
flip(Mo,M)
i = 1
while not np.all(Mo==M):
    Mo = M.copy()
    flip(Mo,M)
    print(i)
    #print(M)
    i+=1
    
print('--- ',np.sum(M==1))