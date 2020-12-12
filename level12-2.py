# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:43:23 2020

@author: Hesiris
"""
from math import e, pi

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
waypoint = 10+1j

for d,v in commands:
    if d in 'NSWE':
        waypoint += dirs[d] * v
    elif d=='F':
        pos += waypoint * v
    elif d in 'LR':
        waypoint *= e**((1 if d=='L' else -1) * v//90 * pi/2* + 1j)
        
    print('{} {:3.0f}  ->  {:3.0f}, {:3.0f}  ({:.0f}, {:.0f})'.
          format(d,v,pos.real,pos.imag,waypoint.real, waypoint.imag))
    
print(round(abs(pos.real)+abs(pos.imag)))