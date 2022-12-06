for _ in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    i = 0
    last = k
    while True:
        if i != n - 1 and h[i] < h[i + 1]:
            k -= 1
            h[i] += 1
        if k < 1:
            print(i + 1)
            break
        i = (1 + i) % n
        if i == 0 and last == k:
            print(-1)
            break
        if i == 0:
            last = k
