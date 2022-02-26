# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:01:02 2022

@author: jjw69
"""

A, B, C = map(int, input().split())
if  C <= B:
    print(-1)
else:
    print(A//(C-B) + 1)