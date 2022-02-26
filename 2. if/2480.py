# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 23:36:30 2022

@author: jjw69
"""

a, b, c = map(int, input().split())
if a == b and a == c:
    print(a * 1000 + 10000)
elif a != b and a != c and b != c:
    print(max(a,b,c) * 100)
elif (a == b and a != c) or (a != b and a == c):
    print(a * 100 + 1000)
else: print(b * 100 + 1000)