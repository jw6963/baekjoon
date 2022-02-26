#10870
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 01:50:12 2022

@author: jjw69
"""
# 피보나치 수열

n = int(input())
def fibo(n):
    if n == 0:
        x = 0
    elif n == 1:
        x = 1
    else:
        x = fibo(n-2) + fibo(n-1)
    return x

print(fibo(n))