# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:42:15 2022

@author: jjw69
"""

S = input()                                                         
num = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]    # 각 번호에 해당하는 문자들
l = []

for i in list(S):                                                   
    for j in num:                                                   
        if i in j:
            l.append(num.index(j) + 3)                              # 입력한 문자의 인덱스 + 3 (2의 인덱스 = 0, 3초 소요)
print(sum(l))