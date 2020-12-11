# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:43:46 2020

@author: Hesiris
"""

from multiprocessing import Pool

def removeable(A, i, removed):
    # if i==len(A)-1:
    #     return False
    i0 = i-1
    while i0 in removed:
        i0-=1
    i1 = i+1
    while i1 in removed:
        i1+=1
        
    
    if i1>len(A)-1:
        return False
    if i0<0:
        return False
    if A[i1] - A[i0]<=3:
        return True
    else:
        return False

def ic(args):
    if len(args)<4:
        print(args)
        print('----')
    A, start, removed, S = args
    for i in range(start,len(A)):
        
        if removeable(A, i, removed):
            
            S+=1
            if S%10_000_000 == 0:
                print('{:,} - ({}) - {}'.format(S,len(removed), removed))
            # print(removed + [i],'ok')
            
            S = ic([A, i+1, removed + [i], S])
        
    return S
        
if __name__ == '__main__':
    
    with open('input-10-1.txt', 'r') as f:
        lines = f.readlines()
        
    
    A = [0] + sorted([int(l) for l in lines])
    print(A)
    print('---------------------\n')
    
    start = 1
    removed = []
    S = 1
    args = []
    for i in range(start,len(A)):
        
        if removeable(A, i, removed):
            
            #S+=1
            if S%1_000 == 0:
                print(S, removed)
            # print(removed + [i],'ok')
            args.append( [A, i+1, removed + [i], S])
    
    with Pool(12) as p:
        res = p.map(ic, args)
        
    print('--------')
    print(sum(res)+1)