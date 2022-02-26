# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:08:26 2022

@author: jjw69
"""
'''
N = int(input())

for i in range(N):
    print((("*")*(1+2*i)).center(1 + 2 * (N-1)))
'''
N = int(input())

for i in range(N):
    print(" "*(N-(i+1)),"*"*(1 + 2 * i), sep = "")