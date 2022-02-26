# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:46:43 2022

@author: jjw69
"""
"""
# 1번째 시도
T = int(input()) # 테스트 케이스 수

for t in range(T):
    S = input()                     # 반복할 횟수와 문자열 입력
    L = [0] * len(S)                
    cnt = 0
    
    for i in S:                     # 문자열 인덱싱
        L[cnt] = i                  
        cnt += 1
    
    R = L[0]                        # 반복할 횟수
    nS = L[2:]                      # 반복할 문자열
    result = []

    for j in nS:
        result.append(int(R) * j)

    result = "".join(result)
    print(result)
"""
"""# 2번째 
T = int(input()) 

for t in range(T):
    S = input()                    
    L = list(S)
    result = []

    for j in L[2:]:
        result.append(int(L[0]) * j)

    result = "".join(result)
    print(result)
# 길이는 줄었지만 시간은 늘어남. ?
"""
# 3번째
T = int(input()) 

for t in range(T):
    R, S = map(str, input().split())                    
    L = list(S)
    result = []

    for j in L:
        result.append(int(R) * j)

    result = "".join(result)
    print(result)