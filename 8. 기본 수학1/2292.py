# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:46:40 2022

@author: jjw69
"""
"""
#메모리 초과
N = int(input())
max = [1] * N
result = 0
for i in range(N):
    max[i] = max[i - 1] + (6 * i)
    if N > max[i]:
        continue
    elif max[i - 1] < N <= max[i]:
        result = i
print(result + 1)
"""
N = int(input())
    
max = [1]
result = 0
i = 0
while True:
    max.append(max[i] + 6 * (i + 1))    # 각 층별 최대치를 리스트에 추가
    if  N <= max[i]:                    # max[i] 보다 같거나 작으면 i층 방
        result = i
        break
    elif N == 1:
        break
    i += 1
print(result + 1)                       # N = 1 일 때, 1이 출력되도록
print(max)