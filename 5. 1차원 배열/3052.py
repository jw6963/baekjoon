# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 23:21:02 2022

@author: jjw69
"""
"""
a = list(int(input()) for i in range(10))
n = [0]*10
for i in range(10):
    n[i] = a[i] % 42
print(len(n))
"""
a = list(int(input()) for i in range(10))
n = [0]*10
for i in range(10):
    n[i] = a[i] % 42
n = set(n)
print(len(n))