# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:00:41 2022

@author: jjw69
"""

a = list(int(input()) for i in range(9))
print(max(a))
print(a.index(max(a)) + 1)