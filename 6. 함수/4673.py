# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 23:59:12 2022

@author: jjw69
"""

def selfnumber(num):   
    All = list(range(1, num + 1))   # 1부터 num까지 숫자 리스트 생성
    
    for i in range(1, num + 1):     # 생성자 있는 숫자 구하기
        S = str(i)                  # 숫자를 각 자리 수로 나누기 위해 문자열로 변환
        L = list(map(int,list(S)))  # L리스트에 각 자리 수 별로 인트형으로 저장
        A = i + sum(L)              # 본수 = 본수 더하기 각 자리수의 생성자
        
        if A in All:                
            All.remove(A)           # All에서 A를 제거(생성자가 있는 수)
            
    for j in All:
        print(j)
        
    return 

selfnumber(10000)