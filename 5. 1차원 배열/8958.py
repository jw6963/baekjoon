# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 17:29:18 2022

@author: jjw69
"""

N = int(input())
for i in range(N):
    a = list(str(input()))
    scr = 0
    cnt = 0
    for j in range(len(a)):
        if a[j] == "O":
            if j == 0:
                scr = 1
            elif j != 0 and a[j-1] == "O" and a[j] == "O":
                cnt += 1
                scr += cnt + 1
            elif j != 0 and a[j-1] == "X" and a[j] == "O":
                scr += 1
        elif a[j] == "X":
            scr = scr
            cnt = 0
    print(scr)

"""
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)          
"""