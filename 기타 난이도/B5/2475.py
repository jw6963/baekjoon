# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:36:18 2022

@author: jjw69
"""
# 검증수
l = list(map(int, input().split()))
a = []
for i in l:
    a.append(i**2)
print(sum(a)%10)