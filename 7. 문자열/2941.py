# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 20:24:44 2022

@author: jjw69
"""

S = input()                     # 문자열 입력
while True:
   S = S.replace("c=", "c")     # 크로아티아 알파벳 치환
   S = S.replace("c-", "c")
   S = S.replace("dz=", "d")
   S = S.replace("d-", "d")
   S = S.replace("lj", "l")
   S = S.replace("nj", "n")
   S = S.replace("s=", "s")
   S = S.replace("z=", "z")
   break
print(len(S))                   # 문자 갯수 세기
