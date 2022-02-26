# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:20:13 2022

@author: jjw69
"""

M = int(input())
N = int(input())
n = list(range(M,N+1))
L = []

for i in n:
    false = 0
    if i > 1:                           # 소수는 2 이상
        for j in range(2, i):           # 2부터 i까지
            if i % j == 0:              # 나누어 떨어지는 수가 있으면
                false += 1              # 소수가 아님
                break                   # 종료 하지 않을 시, 시간 초과
        if false == 0:                  # 나누어 떨어지지 않는 수
            L.append(i)                 # 리스트 L에 추가   
if L ==[]:
    print(-1)                           # 소수가 없으면 -1 출력
else:
    print(sum(L))                       # 소수의 합
    print(min(L))                       # 최솟값 출력