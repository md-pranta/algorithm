import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n, x, t = M()

    a = min(n, t//x)
    print((a-1)*a//2 + max(0, n-a)*a)
