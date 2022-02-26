# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:25:56 2022

@author: jjw69
"""

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x                        # 거리 = y - x
    cnt = 0                             # 움직인 횟수
    move = 1                            # 움직이는 거리
    sum = 0                             # 움직인 거리
    while sum < dist:
        cnt += 1
        sum += move
        if cnt % 2 == 0:                # 횟수가 짝수일 때마다 이동할 거리가 늘어남
            move += 1
    print(cnt)
