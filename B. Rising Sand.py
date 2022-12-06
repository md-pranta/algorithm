for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k == 1:
        print((n - 1) // 2)
    else:
        print(sum(a[i - 1] + a[i + 1] < a[i] for i in range(1, n - 1)))
