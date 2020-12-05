# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:37:46 2020

@author: Hesiris
"""

S = 0
L = ''
with open('input-4-1.txt', 'r') as f:
    for l in f:
        if l == '\n':
            entry = L.split(' ')
            req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #cid
            pp = {}
            for field in entry:
                if len(field)>=1:
                    k,v = field.split(':')
                pp[k] = v
            for r in req:
                if r not in pp:
                    break
            else:
                try:
                    val = int(pp['byr'])
                    if val<1920 or val>2002:
                        print(val)
                        continue
                    
                    val = int(pp['iyr'])
                    if val<2010 or val>2020:
                        print(val)
                        continue
                    
                    val = int(pp['eyr'])
                    if val<2020 or val>2030:
                        print(val)
                        continue
                    
                    val = pp['hgt']
                    if not ((val[-2:]=='cm' and int(val[:-2])>=150 and int(val[:-2])<=193) or\
                        (val[-2:]=='in' and int(val[:-2])>=59 and int(val[:-2])<=76)):
                        print(val)
                        continue
                    
                    val = pp['hcl']
                    if not (val[0]=='#' and len(val)==7 and int(val[1:],16)):
                        print(val)
                        continue
                    
                    val = pp['ecl']
                    if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        print(val)
                        continue
                    
                    val = pp['pid']
                    if len(val)!=9:
                        print(val)
                        continue
                    int(val)
                except Exception as e:
                    print(e)
                    continue
                print('Valid:', pp)
                S+=1
            L= ''
        else:
            L += l[:-1] + ' '
            