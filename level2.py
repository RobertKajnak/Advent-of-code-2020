# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:36:57 2020

@author: Hesiris
"""

S = 0
with open('input-2-1.txt') as f:
    for l in f:
        mn = int(l.split('-')[0])
        mx = int(l.split(' ')[0].split('-')[1])
        letter = l.split(' ')[1][0]
        pwd = l.split(' ')[-1]
        ##occ = pwd.count(letter)
        #print(mn,mx,letter, pwd[:-1])
        #print(occ)
        ##if occ<=mx and occ>=mn:
        ##    S+=1
        
        if (pwd[mn-1] == letter) ^ (pwd[mx-1]==letter):
            S+=1
            
print(S)