# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:35:06 2022

@author: jjw69
"""

N = int(input())
result = 0
while N >= 0:
    if N % 5 == 0:          # N이 5의 배수이면
        result += N // 5    # 결과에 N로 나눈 값을 더하기
        print(result)
        break
    
    N -= 3                  # 5의 배수가 아닐 때 N에서 3씩 차감
    result += 1             # 1씩 추가
    
    if N < 0:               # N값이 위에서 계산이 마무리가 되지 않았을 때
        print(-1)           # -1 출력
        break
