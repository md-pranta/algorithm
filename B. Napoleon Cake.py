for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = []
    c = a[-1]
    for i in range(n - 1, -1, -1):
        c = max(c, a[i])
        if c > 0:
            c -= 1
            ans.append(1)
        else:
            ans.append(0)
    ans.reverse()
    print(*ans)