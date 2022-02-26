# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 14:02:11 2021

@author: jjw69
"""
import sys

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
