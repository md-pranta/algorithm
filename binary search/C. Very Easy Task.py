global n, x, y
def ok(time):
    if time < min(x, y):
        return False
    time -= min(x, y)
    a = time // x + time // y + 1
    return a >= n


n, x, y = map(int, input().split())
l = 0
r = re = n * min(x, y)
while l <= r:
    mid = (l + r) >> 1
    if ok(mid):
        re = mid
        r = mid - 1
    else:
        l = mid + 1
print(re)