# 부분수열의 합
from sys import stdin
from itertools import combinations
input = stdin.readline

N, S = map(int, input().split())        # 수열의 크기와 목표 값
n = list(map(int, input().split()))     # 수열의 값
cnt = 0

for i in range(1, N + 1):               
    comb = list(combinations(n, i))     # 가능한 조합생성 중복x
    for j in comb:
        if sum(j) == S:                 # 해당 조합과 목표 값이 같으면
            cnt += 1                    # cnt + 1
print(cnt)
