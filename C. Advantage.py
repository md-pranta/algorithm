for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s_a = sorted(a)
    first = s_a[-1]
    send = s_a[-2]
    l = []
    for i in range(n):
        if a[i] == first:
            l.append(a[i] - send)
        else:
            l.append(a[i] - first)
    print(*l)