def check(a, b, k, n):
    crnt = n + k - (n +k)// 4
    temp = min(k, crnt)
    crnt -= temp
    res = temp * 100 + sum(a[i] for i in range(crnt))
    cnt = (n + k) - (n + k) // 4
    res2 = sum(b[i] for i in range(min(cnt, n)))
    return res >= res2


for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)
    b = sorted(map(int, input().split()), reverse=True)
    l, r = 0, n
    s = 0
    while l <= r:
        mid = (l + r) >> 1

        if check(a, b, mid, n):
            s = mid
            r = mid - 1
        else:
            l = mid + 1
    print(s)
