for _ in range(int(input())):
    n, m, x, y, d = map(int, input().split())
    if (n - x) + (m - y) > d:
        if (n - x > d and y - 1 > d) or (x - 1 > d and m - y > d):
            print(n + m - 2)
        else:
            print(-1)
    else:
        print(-1)
