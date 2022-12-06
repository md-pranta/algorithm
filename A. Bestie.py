from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if 1 in a:
        print(0)
    else:
        g = 300
        m = min(a)
        f = 1
        for i in range(n):
            g = gcd(m, a[i])
            if g == 1:
                print(0)
                f = 0
                break
        if f:
            li = []
            cost = 0
            for j in range(n - 1, -1, -1):
                k = gcd(i + 1, a[j])
                c = n - 1 + j + 1
                if gcd(g, k) == 1:
                    print(c)
                    break
