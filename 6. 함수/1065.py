# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:22:15 2022

@author: jjw69
"""

def hannum(N):
    cnt = 0                                                 # 한수의 수
    
    for i in range(1, N + 1):                               
        S = str(i)
        L = list(map(int,list(S)))                          # 각 자리 수 구하기
        
        if len(L) < 3:                                      # 두 자리 수 이하는 모두 등차수열
            cnt += 1
            
        elif len(L) == 3 and L[0] - L[1] == L[1] - L[2]:    # 세 자리 수 등차수열 카운트
            cnt += 1
    
    return cnt

N = int(input())
print(hannum(N))