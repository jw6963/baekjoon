# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 16:41:11 2021

@author: jjw69
"""

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break            