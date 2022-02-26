# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:01:00 2022

@author: jjw69
"""

N = int(input())
cnt = N
for _ in range(N):
    S = input()
    for i in range(len(S)- 1):
        if S[i] == S[i + 1]:
            continue
        elif S[i] in S[i + 1:]:
            cnt -= 1
             
print(cnt)