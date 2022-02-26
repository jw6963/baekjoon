# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:25:29 2022

@author: jjw69
"""

N = int(input())
n = list(map(int, input().split()))
cnt = 0

for i in n:
    false = 0
    if i > 1:                           # 소수는 2 이상
        for j in range(2, i):           # 2부터 i까지
            if i % j == 0:              # 나누어 떨어지는 수가 있으면
                false += 1              # 소수가 아님
        if false == 0:                  # 나누어 떨어지지 않는 수
            cnt += 1                    # 카운트 + 1
           
print(cnt)