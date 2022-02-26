# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:13:43 2022

@author: jjw69
"""
# TV 크기
import math
D, H, W = map(int, input().split())

hei = H * D / math.sqrt(H**2 + W**2)
wid = W * D / math.sqrt(H**2 + W**2)
print(math.trunc(hei), math.trunc(wid))