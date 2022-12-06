import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n = N()
    a = L()
    k = 0
    li = []
    for i in range(0, n, 2):
        j = i + 1
        if a[i] == a[j]:
            k += 4
            li += [2, i+1, j+1]
            li += [2, i+1, j+1]
            li += [1, i+1, j+1]
            li += [1, i+1, j+1]
        else:
            k += 6
            li += [1, i+1, j+1]
            li += [2, i+1, j+1]
            li += [1, i+1, j+1]
            li += [1, i+1, j+1]
            li += [2, i+1, j+1]
            li += [1, i+1, j+1]
    print(k)
    x = 0
    while k:
        print(*li[x:x+3])
        x += 3
        k -= 1

