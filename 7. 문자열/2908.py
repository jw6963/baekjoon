# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 23:17:14 2022

@author: jjw69
"""

A, B = map(int, input().split())
rev_A = str(A)[:: -1]               # 숫자 뒤집기
rev_B = str(B)[:: -1]               # str로 바꿔야 [::-1] 가능
if int(rev_A) > int(rev_B):
    print(rev_A)
elif int(rev_A) < int(rev_B):
    print(rev_B)