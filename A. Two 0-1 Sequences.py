for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    if (b == b[0] + a[n - m + 1::]) and b[0] in a[: n - m + 1]:
        print('YES')
    else:
        print('NO')
