for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        x = a[i:n:k]
        ans += max(x)
    print(ans)