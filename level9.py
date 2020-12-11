# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:57:26 2020

@author: Hesiris
"""


with open('input-9-1.txt', 'r') as f:
    lines = f.readlines()
    
A = [int(l) for l in lines]
wl = 25

def get_sum(arr,target):
    smaller = []
    larger = []
    
    for l in arr:
        if l<target//2+1:
            smaller.append(int(l))
        else:
            larger.append(int(l))
    
    for s in smaller:
        for s2 in larger:
            if s+s2==target:
                return True
    return False

#print(A)

for i in range(wl,len(A)):
    if get_sum(A[i-wl:i], A[i]) == False:
        print(A[i])
        target = A[i]
            
        
for i,v in enumerate(A):
    S = 0
    j = 0
    while S<target:
        S+= A[i+j]
        j+=1
        
    if S==target:
        print('---')
        for k in range(i,i+j):
            print(A[k])
            
        print('KEY=',min(A[i:i+j]) + max(A[i:i+j]))
            
        print('---')
        print(i,j)