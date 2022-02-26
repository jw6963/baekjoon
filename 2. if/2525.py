# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 19:51:27 2022

@author: jjw69
"""

A, B = map(int,input().split())
C = int(input())

if B + C > 59:
    H = A + (B + C) // 60
    M = (B + C) % 60
    if H > 23:
        H = H - 24
    print(H, M)
else:
    H = A
    M = B + C
    print(H, M)