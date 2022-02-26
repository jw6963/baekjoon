# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:02:48 2022

@author: jjw69
"""
import string

S = input()                         # 입력받을 문자열
L = string.ascii_lowercase          # a ~ z 알파벳 집합
N = [0] * len(L)                    # 등장 위치 표현할 리스트
cnt = 0

for i in L:                         # a ~ z까지 찾기 위해
    if i in S:                      # i에 해당되는 알파벳이 S에 있을 경우
        N[cnt] = S.index(i)         # N의 0번부터 해당 위치 삽입
        cnt += 1
        
    else:
        N[cnt] = -1                 # S에 없을 경우 -1
        cnt += 1

print(" ".join(list(map(str,N))))   # " "로 구분하여 출력