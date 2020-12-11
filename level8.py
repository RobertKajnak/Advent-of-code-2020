# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:58:52 2020

@author: Hesiris
"""

acv = 0


with open('input-8-1.txt', 'r') as f:
    lines = f.readlines()

executed = {}
original = lines.copy()
trymod = []
for i,l in enumerate(lines):
    cmd, val = l[:-1].split(' ')
    val = int(val)
    if cmd == 'jmp' or cmd == 'nop':
        trymod.append(i)

for k,v in enumerate(trymod):
    i = 0
    lines = original.copy()
    executed = {}
    acv = 0
    if lines[v][:3] == 'jmp':
        lines[v] = 'nop'+ lines[v][3:]
    else:
        lines[v] = 'jmp' + lines[v][3:]
    print(lines)
    
    while i< len(lines):
        l = lines[i]
        cmd, val = l[:-1].split(' ')
        val = int(val)
        #print(i,':',cmd, val)
        
        if i in executed:
            print(acv)
            break
        executed[i] = True
    
        if cmd == 'acc':
            acv += val
        elif cmd == 'jmp':
            i += val
            continue
        
        i +=1
    else:
        print('Success: ', v, acv)
        break