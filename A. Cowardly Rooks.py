for _ in range(int(input())):
    n, m = map(int, input().split())
    li = [map(int, input().split()) for _ in range(m)]
    if n > m:
        print('YES')
    else:
        print('NO')
