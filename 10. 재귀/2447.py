# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:47:50 2022

@author: jjw69
"""
# 별 찍기-10

N = int(input())
star = [[" "] * N for _ in range(N)]    # 공백으로 채워진 다차원 리스트 생성
def func_star(n, r, c):
    if n == 3:                          # n이 3일 때 형태 (기본 형태)
        star[r][c:c+3] = ['*','*','*']
        star[r+1][c:c+3] = ['*'," ",'*']
        star[r+2][c:c+3] = ['*','*','*']
        return
    
    n = int(n / 3)                      # n이 3의 배수일 때
    func_star(n, r, c)                  # 기본 형태 출력
    func_star(n, r, c + n)              # n만큼 뒤의 행에 기본형태 출력
    func_star(n, r, c + n * 2)          # 2n만큼 ~
    func_star(n, r + n, c)              # n만큼 밑의 열에
    func_star(n, r + n, c + n * 2)      # n만큼 밑의 열에서 2n만큼 뒤의 행에
    func_star(n, r + n * 2, c)          # 2n만큼 밑의 열에
    func_star(n, r + n * 2, c + n)      # 2n만큼 밑과 n만큼 뒤에
    func_star(n, r + n * 2, c + n * 2)  # 2n만큼 밑, 2n만큼 뒤에
                                        # n만큼 밑과 n만큼 뒤는 채우지 않음
    
func_star(N, 0, 0)
for i in range(len(star)):
    print("".join(star[i]))             # join함수로 붙여서 출력