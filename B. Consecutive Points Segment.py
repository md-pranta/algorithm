for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    v = x[-1] - x[0] - n
    print('YES' if v <= 1 else 'NO')