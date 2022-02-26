# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:16:24 2021

@author: jjw69
"""

N = int(input())
for i in range(N):
    print(("*" * (i + 1)).rjust(N))