# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:00:03 2020

@author: Hesiris
"""
import time


start_prog = time.perf_counter()
with open('input-10-1.txt', 'r') as f:
    lines = f.readlines()
    

A = [0] + sorted([int(l) for l in lines])
print(A)
print('---')

diffs = {1:0,2:0,3:1} #start from 1, the final adapter
for i in range(1,len(A)):
    diffs[A[i]-A[i-1]] +=1
    #print(A[i]-A[i-1])
    

print(diffs)
print(diffs[1] * diffs[3])


        
#%% part2 try 4

print('--part 2--')
# def comb(n,k):
#     return math.factorial(n)/math.factorial(k)/math.factorial(n-k)

start = time.perf_counter()
D = []
for i in range(1,len(A)):
    D.append(A[i]-A[i-1])
    
# S = 0
# for i in range(1,len(A2)):
#     if A2[i-1]==A2[i]==1:
#         S+=1
        

#print('D = ', D)
D = [3] + D + [3]
L = []
l=0
for i in range(1,len(D)):
    if D[i-1] == 3 and D[i] == 1:
        l = i
    if D[i-1] == 1 and D[i] == 3:
        if i-l>1:
            L.append(i-l-1)
        l=0
#print('L = ',L)

P = 1
lookup = {1:2,
          2:4,
          3:7,
          4:2**4-6
          }
for l in L:
    P*=lookup[l]
    # P*=2**l-sum(range(l-2))

print('  Calculation time: ',time.perf_counter()-start)
print(P)

print('  With reading and printing:', time.perf_counter()-start_prog)






#%%
# S = 1

# Ab = A.copy()

# for j in range(1,len(A)):
#     for i in range(1,len(A)):
#         if A[i]-A[i-1]>3:
#             break;
#     else:
#         S+=1
        
        
# def is_valid(arr):
#     for i in range(1,len(arr)):
#         if arr[i]-arr[i-1]>3:
#             return False
#     else:
#         return True
            

# def ic(start, end, rem, previt):
#     if rem == 0:
#         #print()
#         pass
#     else:
#         for i in range(start,end-1):
#             if rem == 1:
#                 #print(i, end = ' ')
#                 #print(previt + [i])
#                 Amod = A.copy()
#                 for k in (previt + [i])[::-1]:
#                     del Amod[k]
#                 #print(Amod)
#                 if is_valid(Amod):
#                     #print(previt + [i])
#                     ic.S+=1
#                     ic.novalids = False
#                 # for j in previt+[i]:
#                 #     if A[j-1]-A[j-2]>3:
#                 #         print('bad')
#             else:
#                 Amod = A.copy()
#                 for k in (previt + [i])[::-1]:
#                     if Amod[k+1]-Amod[k-1]<3:
#                         del Amod[k]
#                     else:
#                         print('broken at: ', previt + [i])
#                         break
                    
#                 # if is_valid(Amod):
#                 else:
#                     ic.S += 1
#                     ic(i+1,end,rem-1, previt + [i])
#                 # else:
#                 #     print('broken at: ', previt + [i])
        
# ic.S = 1
# #for i0 in range(1,len(A)-3):
# # print('---', i0)
# ic.novalids = True
# ic(1,len(A),10, previt = [])
# # if ic.novalids:
# #     break

# print('Res = ', ic.S)
        
#%% Part2, try 3
# A2 = []

# # for i in range(len(A)-1,0,-1):
# #     if A[i]-A[i-1] == 3:
# #         print(i)

# def removeable(i,removed):
#     # if i==len(A)-1:
#     #     return False
#     i0 = i-1
#     while i0 in removed:
#         i0-=1
#     i1 = i+1
#     while i1 in removed:
#         i1+=1
        
    
#     if i1>len(A)-1:
#         return False
#     if i0<0:
#         return False
#     if A[i1] - A[i0]<=3:
#         return True
#     else:
#         return False

# def ic(start, removed, S):
    
#     for i in range(start,len(A)):
        
#         if removeable(i, removed):
            
#             S+=1
#             print(S, removed +[i])
#             # print(removed + [i],'ok')
            
#             S = ic(i+1, removed + [i], S)
        
#     return S
# ic.S=1
# S = 1
# removed = []
# S = ic(1, removed, S)
# print('Res = ', S)








