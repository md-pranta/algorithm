for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    c = 0
    for i in map(int, input().split()):
        c += i
        c %= n
    print(a[c])
