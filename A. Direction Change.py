for _ in range(int(input())):
    n, m = map(int, input().split())
    maxi = max(n, m)
    if (n == 1 and m >= 3) or (m == 1 and n >= 3):
        print(-1)
    elif (n + m) & 1:
        print(2 * maxi - 3)
    else:
        print(2*(maxi-1))
