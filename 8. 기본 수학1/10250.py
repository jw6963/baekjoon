# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:13:12 2022

@author: jjw69
"""

T = int(input())
result = []
for i in range(T):
    H, W, N = map(int,input().split())
    L = []
    for X in range(1, W + 1):
        for Y in range(1, H + 1):
            if X <10:
                R = "%d0%d"%(Y,X)
            else:
                R = "%d%d"%(Y,X)
            L.append(R)                         # 리스트L에 먼저 들어갈 호수 순으로 추가
    result.append(L[N - 1])
print(*result, sep = "\n")