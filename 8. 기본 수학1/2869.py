# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 18:38:05 2022

@author: jjw69
"""

from math import *
A, B, V = map(int,input().split())
if A >= V:
    print(1)
else:
    print(ceil((V - A) / (A - B)) + 1)