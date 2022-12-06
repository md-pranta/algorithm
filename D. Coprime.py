from math import gcd

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    d = {x: k + 1 for k, x in enumerate(li)}
    res = -1
    b = list(d.keys())
    for i in range(len(b)):
        for j in range(i, len(b)):
            if gcd(b[i], b[j]) == 1:
                res = max(res, d[b[i]] + d[b[j]])
    print(res)
