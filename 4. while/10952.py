# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:37:28 2021

@author: jjw69
"""

while True:
    A, B = map(int, input().split())
    if (A == 0 and B == 0):
        break
    else:
        print(A + B)