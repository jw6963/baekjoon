# 유레카 이론

'''
# 시간초과
def T(n):
    t = int(n*(n+1)/2)
    return t
Test = int(input())
for _ in range(Test):
    l = []
    K = int(input())
    for i in range(1,46):
        if T(i) > K:
            break
        for j in range(1,46):
            if T(j) > K:
                break
            for x in range(1,46):
                if T(x) > K:
                    break
                if K == T(i) + T(j) + T(x):
                    l.append(1)
    if len(l) != 0:
        print(1)
    else:
        print(0)
'''
'''
# 시간초과
from itertools import combinations_with_replacement

T = int(input())
l = [int(x*(x+1)/2) for x in range(1,46)]
for i in range(T):
    K = int(input())
    comb = list(combinations_with_replacement(l,3))
    if sum(comb[i]) == K:
        print(1)
        break
    else: print(0)
'''
'''
# 시간초과
T = int(input())
n = [int(x*(x+1)/2) for x in range(1,45)]
l = [0] * 1001

for _ in range(T):
    K = int(input())
    for i in range(len(n)):
        for j in range(len(n)):
            for k in range(len(n)):
                if n[i] + n[j] + n[k] <= 1000:
                    l[n[i] + n[j] + n[k]] = 1
    print(l[K])
'''
T = int(input())
n = [int(x*(x+1)/2) for x in range(1,45)]
l = [0] * 1001


for i in range(len(n)):
    for j in range(len(n)):
        for k in range(len(n)):
            if n[i] + n[j] + n[k] <= 1000:
                l[n[i] + n[j] + n[k]] = 1
for _ in range(T):
    print(l[int(input())])