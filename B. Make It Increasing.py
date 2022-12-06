for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n - 2, -1, -1):
        while a[i] >= a[i + 1] and a[i] > 0:
            a[i] = a[i] // 2
            count += 1
        if a[i] == a[i + 1]:
            print(-1)
            break
    print(count)
