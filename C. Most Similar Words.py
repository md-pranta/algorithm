def cost(l, a, b):
    return sum(abs(ord(a[k]) - ord(b[k])) for k in range(l))


for _ in range(int(input())):
    n, m = map(int, input().split())

    li = []
    for _ in range(n):
        s1 = input()
        li.append(s1)

    ans = 10000000
    for i in range(n):
        for j in range(i+1, n):
            ans = min(ans, cost(m, li[i], li[j]))
    print(ans)
