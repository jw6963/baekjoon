# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 23:47:03 2022

@author: jjw69
"""
# 킹, 퀸, 룩, 비숍, 나이트, 폰

ori = [1,1,2,2,2,8]
rec = list(map(int,input().split()))
mor = []

for i in range(len(ori)):
    mor.append(str(ori[i] - rec[i]))

print(" ".join(mor))