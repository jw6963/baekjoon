# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:01:00 2022

@author: jjw69
"""
'''
N = int(input())
cnt = N
for _ in range(N):
    S = input()
    for i in range(len(S)- 1):
        if S[i] == S[i + 1]:
            continue
        elif S[i] in S[i + 1:]:
            cnt -= 1
             
print(cnt)
'''
N = int(input())                                # 단어 수
cnt = 0                                         # 그룹단어가 아닌 수

for _ in range(N):
    S = input()                                 # 입력할 단어
    stack = []                                  # 그룹단어 판별을 위한 리스트
    
    for i in S:
        if i not in stack:                      # 스택에 해당 문자가 중복이 없으면 리스트에 추가
            stack.append(i)
            
        elif i in stack and stack[-1] == i:     # 해당 문자가 중복이지만 직전의 문자와 같다면 리스트에 추가
            stack.append(i)
            
        else:                                   # 위 조건을 만족하지 않으면 그룹단어 조건 만족 x
            cnt += 1                            # 그룹단어가 아닌 수 카운트 + 1
            break                               # break로 탈출
print(N - cnt)                                  # 그룹단어의 개수 출력