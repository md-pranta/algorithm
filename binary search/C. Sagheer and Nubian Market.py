n, s = map(int, input().split())
a = list(map(int, input().split()))
l, r = 0, n
k = 0
total_cost = 0
while l <= r:
    mid = (l + r) >> 1
    b = sorted([a[i] + mid * (i + 1) for i in range(n)])
    ans = sum(b[j] for j in range(mid))
    if ans <= s:
        k = mid
        total_cost = ans
        l = mid + 1
    else:
        r = mid - 1
print(k, total_cost)