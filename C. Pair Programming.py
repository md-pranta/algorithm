import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    input()
    k, n, m = M()
    a = L()
    b = L()

    x = y = 0
    li = []
    condition = True
    while x < n or y < m:
        if x < n and a[x] <= k:
            li.append(a[x])
            if not a[x]:
                k += 1
            x += 1
        elif y < m and b[y] <= k:
            li.append(b[y])
            if not b[y]:
                k += 1
            y += 1
        else:
            condition = False
            break
    if condition:
        print(*li)
    else:
        print(-1)