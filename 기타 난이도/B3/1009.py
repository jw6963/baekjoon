# 분산처리
# 시간초과 주의

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    _a = a % 10
    if _a == 0:
        print(10)
    elif _a == 1 or _a == 5 or _a == 6:
        print(_a)
    elif _a == 2:
        if b % 4 == 1:
            print(2)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(8)
        else: print(6)
    elif _a == 3:
        if b % 4 == 1:
            print(3)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(7)
        else: print(1)
    elif _a == 4:
        if b % 2 == 1:
            print(4)
        else: print(6)
    elif _a == 7:
        if b % 4 == 1:
            print(7)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(3)
        else: print(1)
    elif _a == 8:
        if b % 4 == 1:
            print(8)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(2)
        else: print(6)
    elif _a == 9:
        if b % 2 == 1:
            print(9)
        else: print(1)