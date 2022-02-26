# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:09:43 2021

@author: jjw69
"""

year = int(input())
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(1)
else:
    print(0)