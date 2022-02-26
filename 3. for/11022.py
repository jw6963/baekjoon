# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:09:37 2021

@author: jjw69
"""

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i+1, A, B, A+B))