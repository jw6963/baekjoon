# 숫자 야구
from itertools import permutations
from sys import stdin
input = stdin.readline

L = list(permutations([1,2,3,4,5,6,7,8,9],3))
for N in range(int(input())):
    T, S, B = map(int,input().split())  
    T = [int(_) for _ in str(T)]
    cnt = 0

    for i in range(len(L)):
        S_cnt = 0
        B_cnt = 0
        i -= cnt

        for j in range(3):
            if T[j] == L[i][j]:
                S_cnt += 1
            elif T[j] in L[i]:
                B_cnt += 1

        if S_cnt != S or B_cnt != B:
            L.remove(L[i])
            cnt += 1
print(len(L))