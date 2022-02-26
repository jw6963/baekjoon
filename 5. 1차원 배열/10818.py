# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:32:06 2021

@author: jjw69
"""

N = int(input())
a = list(map(int, input().split()))
max = a[0]
min = a[0]
for i in range(N):
    if (a[i] < max):
        max = max
    else:
        max = a[i]
for i in range(N):
    if (a[i] > min):
        min = min
    else:
        min = a[i]
print("최소값: ", min, "최대값:", max, end = " ")