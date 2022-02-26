# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:38:48 2022

@author: jjw69
"""

while True:
    a = sorted(list(map(int, input().split())))     # 각 변의 길이 입력 및 오름차순 정렬
    if sum(a) == 0:                         # 0 0 0 입력 시 종료
        break
    elif a[0]**2 + a[1]**2 == a[2]**2:   # 피타고라스 정리
        print("right")                      # 성립 시 직각삼각형
    else: print("wrong")
    