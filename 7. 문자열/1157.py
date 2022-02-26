# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:24:03 2022

@author: jjw69
"""
"""
# 1번째 시도
S = input()                                     # 문자열 입력
U = S.upper()                                   # 대문자로 변경
sort_U = sorted(U)                              # 문자열 오름차순 정렬
C = [0] * len(set(U))                           # 문자 사용 횟수 담을 리스트
cnt = 0                                         # 문자 사용 횟수
c = 0                                           # 리스트 인덱스 번호

for i in range(len(U)):                         
    if i == 0:                                  # 첫번째 문자라서 
        cnt = 1                                 # 무조건 카운트 1
    elif sort_U[i] == sort_U[i - 1]:            # 이전 문자와 현재 문자가 같으면 카운트1 (오름차순 했기 때문에 뒤에 더 안나옴)
        cnt += 1
        if i == len(U) - 1:
            C[c] = cnt
    elif sort_U[i] != sort_U[i - 1]:            # 이전 문자와 현재 문자가 다르면 리스트에 이전 문자 횟수 추가
        C[c] = cnt    
        c += 1                                  # 인덱스 넘어감
        cnt = 1                                 # 카운트 횟수 초기화
        if i == len(U) - 1:
            C[c] = cnt
        
if C.count(max(C)) > 1:                         # 최대 사용횟수가 둘 이상이면 ?출력
    print("?")        
elif C.count(max(C)) == 1:                      # 최대 사용 횟수가 하나면 그 문자 출력
    print(list(sorted(set(U)))[C.index(max(C))])# 가장 높은 사용횟수의 C리스트의 인덱스 번호 = (중복을 제거한)오름차순 문자의 위치

"""
# 2번째 시도
S = input()                                     
U = S.upper()                                   
ssu = sorted(set(U))                    # 중복 제거 및 정렬
C = []                

for i in ssu:                           
    C.append(U.count(i))                # 각 문자가 쓰인 횟수 저장
    
if C.count(max(C)) > 1:                        
    print("?")        
    
elif C.count(max(C)) == 1:                    
    print(list(ssu)[C.index(max(C))])
