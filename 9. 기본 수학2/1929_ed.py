# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 22:41:18 2022

@author: jjw69
"""

M, N = map(int, input().split())
L = []

for i in range(M, N + 1):
    false = 0
    
    if i > 1:                           
        for j in range(2, i):
            if i % j == 0:
                false += 1
                break
            
        if false == 0:
            L.append(i)

for x in range(len(L)):
    print(L[x])