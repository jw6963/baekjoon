# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:53:25 2022

@author: jjw69
"""
N = int(input())
a = input()
l = []
for i in a:
    l.append(i)
l = list(map(int,l)) #문자열 리스트를 int 리스트로 변환
print(sum(l))