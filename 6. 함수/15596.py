# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:32:03 2021

@author: jjw69
"""

def solve(a):
    sum = 0
    n = int(input("정수의 개수: "))
    for i in range(n):
        sum = sum + a[i]
        return sum
    
a = list(map(int, input().split()))
result = solve(a)
print(result)