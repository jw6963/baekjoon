# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:49:40 2022

@author: jjw69
"""
# 하노이 탑 이동 순서

N = int(input())        # 원판의 수
def hanoi(n,A,B,C):
    if n == 1:          # 1개일 때
        print(A,C)      # 1번에서 3번으로
        return
    hanoi(n-1,A,C,B)    # 마지막 원판을 제외한 원판들을 1번에서 2번으로 보내기
    print(A,C)          # 1번에 남아있던 마지막 원판을 3번으로
    hanoi(n-1,B,A,C)    # 2번으로 보냈던 나머지 원판들을 3번으로

print(2**N - 1)         # 이동 횟수
hanoi(N,1,2,3)