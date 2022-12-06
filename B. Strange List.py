for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    arr = a[:]
    ans = sum(a)
    i = 0
    while not a[i] % x:
        ans += arr[i]
        a[i] //= x
        i = (i + 1) % n
    print(ans)
