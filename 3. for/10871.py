# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:21:04 2021

@author: jjw69
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if (A[i] < X):
        print(A[i], end = " ")