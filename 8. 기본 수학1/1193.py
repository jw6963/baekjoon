# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:18:39 2022

@author: jjw69
"""
"""
# 시간초과
X = int(input())
num = 1                                                 # 1부터 시작
den = 1
sum = num + den                                         # 분자와 분모의 합
L = []                                                  # 분수를 담을 리스트
for _ in range(X):
    for i in range(1, sum + 1):                         # 
        if sum % 2 == 0:                                # 합이 짝수일 때
            num = sum - i                               # 분자 값은 1씩 감소
            den = sum - num                             # 분모 값은 1씩 증가
            if num != 0 and den != 0:                   # 분모와 분자가 0인 경우 제외
                L.append(num)                           # 리스트에 분자와 분모 값 추가
                L.append(den)
        elif sum % 2 == 1:                              # 합이 홀수일 때
            den = sum - i                               # 분모 값은 1씩 감소
            num = sum - den                             # 분자 값은 1씩 증가
            if num != 0 and den != 0:
                L.append(num)
                L.append(den)
    sum += 1
if X == 1:                                              # X값이 1인 경우는 1/1출력
    print("1/1")
else:
    print(L[2 * X - 2], "/", L[2 * X - 1], sep = "")    # 순서대로 분자와 분모 값 여백없이 분수로 출력
"""

X = int(input())

line = 0  
max = 0  

while X > max:
    line += 1  
    max += line  

gap = max - X

if line % 2 == 0:  
    num = line - gap  
    den = gap + 1  
    
else :  
    num = gap + 1  
    den = line - gap  
    
print(num, "/", den, sep = "")