# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 16:23:07 2022

@author: jjw69
"""
from math import pi
R = int(input())            # 반지름
print("%.6f"%(R**2 * pi))   # 유클리드 기하학 원의 넓이
print("%.6f"%(R**2 * 2))    # 택시 기하학 원의 넓이