# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:19:10 2022

@author: jjw69
"""

T = int(input())

for _ in range(T):
    k = int(input())                # 층수 입력
    n = int(input())                # 호수 입력
    L = list(range(1, n + 1))       # 1부터 n까지 리스트 생성
    
    for i in range(k):              # 층수만큼 반복
        for j in range(1, n):
            L[j] += L[j-1]          # 이전 층의 j호수의 수를 순서대로 더함
            
    print(L[-1])                    # 마지막 인덱스 출력
