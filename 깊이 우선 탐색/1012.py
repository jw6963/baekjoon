# 유기농 배추
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(3000)                     # 재귀 횟수 기존 1000번에서 3000번으로 증가

def dfs(x, y):                              # 깊이 우선 탐색
    global L
    L[x][y] = 0                             # 해당 좌표 0으로
    if x < N - 1 and L[x + 1][y] == 1:      # 인접한 좌표들이 1이면 재귀호출
        dfs(x+1, y)
    if x > 0 and L[x - 1][y] == 1:
        dfs(x-1, y)
    if y < M - 1 and L[x][y + 1] == 1:
        dfs(x, y + 1)
    if y > 0 and L[x][y - 1] == 1:
        dfs(x, y - 1)
    
for tc in range(int(input())):              # 테스트 케이스 횟수
    M,N,K = map(int, input().split())       # 가로, 세로, 배추의 수
    L = [[0] * M for _ in range(N)]         # 밭의 크기
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())    # 배추의 위치
        L[y][x] = 1
    for i in range(N):
        for j in range(M):
            if L[i][j] == 1:                # 1 탐색
                dfs(i, j)
                cnt += 1
    print(cnt)