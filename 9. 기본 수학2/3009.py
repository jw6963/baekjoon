# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 23:33:33 2022

@author: jjw69
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2 and y1 == y2:
    x4 = x3
    y4 = y3
elif x1 == x2 and y1 == y3:
    x4 = x3
    y4 = y2
elif x1 == x2 and y2 == y3:
    x4 = x3
    y4 = y1
elif x1 == x3 and y1 == y2:
    x4 = x2
    y4 = y3
elif x1 == x3 and y1 == y3:
    x4 = x2
    y4 = y2
elif x1 == x3 and y2 == y3:
    x4 = x2
    y4 = y1    
elif x2 == x3 and y1 == y2:
    x4 = x1
    y4 = y3
elif x2 == x3 and y1 == y3:
    x4 = x1
    y4 = y2
elif x2 == x3 and y2 == y3:    
    x4 = x1
    y4 = y1
print(x4, y4)