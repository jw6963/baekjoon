# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:52:55 2022

@author: jjw69
"""
# 일곱 난쟁이

L = [int(input()) for _ in range(9)]    # 아홉 난쟁이의 키
L.sort()                                # 오름차순 정렬

sum = sum(L)                            # 아홉 난쟁이의 키 전체 합
for i in range(9):                      # 9번까지 중의 하나와
    for j in range(i+1,9):              # i를 제외한 하나
        if sum - (L[j] + L[i]) == 100:  # 의 키의 합이 100일 때
            not_dwarfs1 = L[i]          # L[i]와 L[j]를 제외한 나머지가 일곱 난쟁이
            not_dwarfs2 = L[j]

L.remove(not_dwarfs1)
L.remove(not_dwarfs2)

for a in L:                             # 오름차순으로 한 줄씩 출력
    print(a)