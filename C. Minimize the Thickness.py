for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = n
    s = sum(a)
    ttt = a
    for xxx in range(n):
        x = s - ttt[xxx]
        s = x
        l = -1
        key = 1
        curr = 0
        temp = 0
        for i in range(n):
            curr += a[i]
            temp += 1
            if curr >= x:
                l = max(l, temp)
                temp = 0
                if (curr != x):
                    key = 0
                    break
                curr = 0
        if key and curr == 0:
            ans = min(ans, l)
    print(ans)
