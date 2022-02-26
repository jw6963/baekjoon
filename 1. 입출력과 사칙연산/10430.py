# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 20:44:06 2021

@author: jjw69
"""

A, B, C = map(int, input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)