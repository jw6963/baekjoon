# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:58:29 2021

@author: jjw69
"""

N = int(input())
cnt = 0
new = N
while True:
    a = new // 10
    b = new % 10
    c = (a + b) % 10
    new = b*10 + c
    cnt += 1
    if (new == N):
        print(cnt)
        break