# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 15:18:24 2022

@author: jjw69
"""
import math
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt(((x1 - x2)**2 + (y1 - y2)**2))     # 중심원 사이의 거리
    if dist == 0 and r1 == r2:                          # 겹치는 원
        print(-1)
    elif dist == abs(r1 - r2) or dist == r1 + r2:       # 내접 or 외접하는 경우
        print(1)
    elif abs(r1 - r2) < dist < (r1 + r2):               # 두 점에서 만나는 경우
        print(2)
    else: print(0)