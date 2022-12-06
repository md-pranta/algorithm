import math

for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    g = 0
    for i in range(n):
        g = math.gcd(a[i], g)
    print(a[n - 1] // g)

"""
    for i in range(1, n):
        if a[i] % a[0]:
            print(a[-1])
            break
    else:
        print(a[-1]//a[0])
"""
