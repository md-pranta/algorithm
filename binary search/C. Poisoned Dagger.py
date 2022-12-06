for _ in range(int(input())):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    l = 1
    r = h
    while l <= r:
        mid = sum = (l + r) >> 1
        for i in range(n-1):
            sum += min(mid, a[i+1] - a[i])
        if sum < h:
            l = mid + 1
        else:
            r = mid - 1
    print(r + 1)