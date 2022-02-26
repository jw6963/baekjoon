# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:11:30 2022

@author: jjw69
"""

N = int(input())
a = list(map(int, input().split()))
n = [0]*N
for i in range(N):
    n[i] = (a[i] / max(a)) * 100
print(sum(n)/N)