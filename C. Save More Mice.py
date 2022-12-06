import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return sorted(map(int, sys.stdin.readline().split()), reverse=True)
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n, k = M()
    li = L()
    saved = 0
    cat = 0
    for i in range(k):
        if li[i] > cat:
            saved += 1
            cat += n - li[i]
        else:
            break
    print(saved)