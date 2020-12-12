# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:43:23 2020

@author: Hesiris
"""

import numpy as np

commands = []

with open('input-12-1.txt', 'r') as f:
    for l in f:
        if len(l)>1:
            commands.append((l[0],int(l[1:])))

pos = np.zeros(2,dtype='int')
dirs ={'N':np.array((0,1)),
       'E':np.array((1,0)),
       'S':np.array((0,-1)),
       'W':np.array((-1,0))
       }
ori = ('N','E','S','W')
cdir = 1

for d,v in commands:
    if d in 'NSWE':
        pos += dirs[d] * v
    elif d=='F':
        pos += dirs[ori[cdir]] * v
    elif d in 'LR':
        cdir = (cdir + (1 if d=='R' else -1) * v//90)%4
    print('{} {:3}  ->  {:3}, {:3}  ({})'.format(d,v,*pos,ori[cdir]))
    
print(sum(abs(pos)))