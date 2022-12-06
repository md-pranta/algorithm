import sys

input = lambda: sys.stdin.readline().strip()
t = int(input())
for _ in range(t):
    n = int(input())
    nstr = input()
    ans = 0
    for i in range(1, n + 1):
        div = 0
        temp = [0] * 10
        vis = set([])
        for j in range(i, n + 1):
            if nstr[j - 1] not in vis:
                div += 1
                vis.add(nstr[j - 1])
            temp[int(nstr[j - 1])] += 1
            if max(temp) <= div:
                ans += 1
            if max(temp) > 10:
                break
    print(ans)
