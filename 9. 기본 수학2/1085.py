# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 17:44:54 2022

@author: jjw69
"""
'''
x, y, w, h = map(int, input().split())
if w - x < x and h - y < y:
    a = w - x
    b = h - y
    if a <= b:
        print(a)
    else:
        print(b)
elif w - x < x and h - y > y:
    a = w - x
    b = y
    if a <= b:
        print(a)
    else:
        print(b)
elif x < w - x and h - y < y:
    a = x
    b = h - y
    if a <= b:
        print(a)
    else:
        print(b)
elif x < w - x and h - y > y:
    a = x
    b = y
    if a <= b:
        print(a)
    else:
        print(b)
'''
x, y, w, h = map(int, input().split())
print(min(x, y, w - x, h - y))