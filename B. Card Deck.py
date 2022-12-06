for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    out = []
    i = 0
    for j in range(i, n):
        if a[j] > a[i]:
            out += a[i:j][::-1]
            i = j
    out += a[i:n][::-1]
    print(*out[::-1])