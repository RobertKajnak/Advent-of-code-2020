# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:56:07 2020

@author: Hesiris
"""
from pprint import pprint

bag_lookup = {}

def can_contain(bag, target):
    if bag in bag_lookup:
        if target in bag_lookup[bag]:
            #print(bag)
            return True
        else:
            for b in bag_lookup[bag].keys():
                cc = can_contain(b, target)
                if cc:
                    return True
    return False

with open('input-7-1.txt', 'r') as f:
    for l in f:
        l = l[:-2]
        parent = l.split('bags')[0][:-1]
        children = l[len(parent)+5+8:].split(',')
        #print(parent)
        ch_lst = {}
        for child in children:
            if child[:3]==' no':
                count = 0
                val = None
            else:
                count = int(child[:3])
                val = child[3:].replace('bags','').replace('bag','').rstrip()
                ch_lst[val] = count
        bag_lookup[parent] = ch_lst
        if count>9:
            print(parent)
            #print('  ',count, val)
        #print(parent,';',children)
            
    
S = 0
for b in bag_lookup.keys():
    if can_contain(b,'shiny gold'):
        S+=1
        
#pprint(bag_lookup)
print(S)

#%% Part 2

def get_sum(bag):
    if bag in bag_lookup and bag_lookup[bag]:
        subs = 0 
        for subbag,cnt in bag_lookup[bag].items():
            print(subbag)
            subs += get_sum(subbag) * cnt
            print(subbag, subs)
        return subs+1
    print('endpoint: ', bag)
    return 1

print('Bags req:', get_sum('shiny gold')-1)
