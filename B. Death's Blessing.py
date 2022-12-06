for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    t = b[0]
    for i in range(n):
        ans += a[i] + b[i]
        if t < b[i]:
            t = b[i]
    print(ans-t)

