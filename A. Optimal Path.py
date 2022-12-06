for _ in range(int(input())):
    n, m = map(int, input().split())
    x = (m * (m + 1))//2
    y = (n * (n + 1))//2
    y = y * m - m
    print(x + y)
