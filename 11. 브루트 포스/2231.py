# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:59:38 2022

@author: jjw69
"""
# 분해합

N = input()                                     # 자리수 별로 나누기 위해 str로 input
c = []

def create(n):                                  # 분해합을 구하는 함수
    l = [int(n[x]) for x in range(len(str(n)))] # n의 각 자리수를 int형으로 담은 리스트
    Created = int(n) + sum(l)                   # 분해합
    return Created
    
for i in range(int(N) - len(N)*9,int(N)):       # 생성자의 최솟값~최댓값 범위
     if i > 0 and create(str(i)) == int(N):     # i가 양수일 때, N의 생성자 구하기
         c.append(i)                            # 리스트 c에 생성자 값 추가
         break
     
if len(c) == 0:                                 # 생성자가 없으면 0 출력
        print(0)
        
else: print(c[0])                               # 있으면 생성자 출력