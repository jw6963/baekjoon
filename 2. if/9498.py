# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 18:03:36 2021

@author: jjw69
"""

score = int(input())
if (90 <= score <= 100):
    print("A")
elif (80 <= score < 90):
    print("B")
elif (70 <= score < 80):
    print("C")
elif (60 <= score < 70):
    print("D")
else:
    print("F")