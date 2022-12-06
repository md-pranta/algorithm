for _ in range(int(input())):
    n = int(input())
    a = list(range(1, 1 + n))
    ans = []
    while len(a) != 1:
        ans.append([a[-1], a[-2]])
        a.append((a[-1] + a[-2] + 1) // 2)
        a.pop(n - 2)
        a.pop(n - 2)
        n -= 1
    print(*a)
    for item in ans:
        print(*item)
