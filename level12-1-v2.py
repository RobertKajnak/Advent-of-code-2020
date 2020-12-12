# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:43:23 2020

@author: Hesiris
"""

commands = []

with open('input-12-1.txt', 'r') as f:
    for l in f:
        if len(l)>1:
            commands.append((l[0],int(l[1:])))

pos = 0
dirs ={'N': 1j,
       'E': 1,
       'S':-1j,
       'W':-1
       }
ori = ('N','E','S','W')
cdir = 1
waypoint = 10+1j

for d,v in commands:
    if d in 'NSWE':
        pos += dirs[d] * v
    elif d=='F':
        pos += dirs[ori[cdir]] * v
    elif d in 'LR':
        cdir = (cdir + (1 if d=='R' else -1) * v//90)%4
    print('{} {:3}  ->  {:3}, {:3}  ({})'.format(d,v,pos.real,pos.imag,ori[cdir]))
    
print(abs(pos.real)+abs(pos.imag))