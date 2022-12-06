global n, k, b


def ok(x):
    s = 0
    for i in range(n):
        s += b[i] / x
    return s >= k


n, k = map(int, input().split())
b = [int(input()) for _ in range(n)]
l = 0
r = 1000
for _ in range(100):
    mid = (l + r) / 2
    if ok(mid):
        l = mid
    else:
        r = mid
print(l)
