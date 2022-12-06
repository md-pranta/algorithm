a, b, n = map(int, input().split())
l = 0
r = max(n, a * b)
ans = n
while l <= r:
    mid = (l + r) >> 1
    if (mid // a) * (mid//b) >= n:
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)