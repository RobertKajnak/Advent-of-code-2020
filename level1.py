# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:01:01 2020

@author: Hesiris
"""


smaller = []
larger = []

with open('input-1-1.txt') as f:
    for l in f:
        if int(l)<1010:
            smaller.append(int(l))
        else:
            larger.append(int(l))

for s in smaller:
    for s2 in smaller:
        for l in smaller:
            if s+s2+l==2020:
                print(s,s2,l,s*s2*l)