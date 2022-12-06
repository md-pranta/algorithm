for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != min(a):
        print('NO')
    else:
        print('YES')