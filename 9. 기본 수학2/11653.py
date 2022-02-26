# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:32:51 2022

@author: jjw69
"""

N = int(input())
for i in range(2, N + 1):   # 소수
    while N % i == 0:       # 나누어지는 수
        print(i)
        N = N // i