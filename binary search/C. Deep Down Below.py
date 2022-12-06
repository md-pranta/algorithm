for _ in range(int(input())):
    n = int(input())
    li = []
    for _ in range(n):
        maximum = -1
        a = list(map(int, input().split()))
        for k in range(1, a[0]+1):
            maximum = max(maximum, a[k]-k + 2)
        li.append([a[0], maximum])
    li.sort(key=lambda y: y[1])
    l, r = li[0][1], li[-1][-1]
    ans = r
    while l <= r:
        ok = 1
        mid = po = (l + r) >> 1
        for i in range(n):
            if po >= li[i][1]:
                po += li[i][0]
            else:
                ok = 0
                break
        if ok:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)

