for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = max(a)
    k = 0
    most = -1
    for i in range(n-1, -1, -1):
        if x == a[i]:
            print(k)
            break
        if most < a[i]:
            k += 1
            most = a[i]