import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = math.inf
    for i in range(33):
        d = a
        c = 0
        if i + b == 1:
            continue
        while d:
            d //= b + i
            c += 1
        ans = min(ans, c + i)

    print(ans)
