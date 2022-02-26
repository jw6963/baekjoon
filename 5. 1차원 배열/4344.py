# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 23:46:07 2022

@author: jjw69
"""

C = int(input())

for _ in range(C):
    S = list(map(int,input().split()))
    N = S[0]
    avg = sum(S[1:]) / N
    cnt = 0
    for i in range(N):
        if S[i+1] > avg:
            cnt += 1
        rate = (cnt/N) * 100
    print("%.3f%%" %rate)