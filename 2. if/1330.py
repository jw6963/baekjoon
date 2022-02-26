# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:00:10 2021

@author: jjw69
"""

A, B = map(int, input().split())
if (A > B):
    print('>')
elif (A < B):
    print('<')
else:
    print("==")