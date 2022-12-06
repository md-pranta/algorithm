import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n = N()
    k = 1
    while 2 * k <= n - 1:
        k *= 2
    for i in range(k - 1, -1, -1):
        print(i, end=' ')
    for i in range(k, n):
        print(i, end=' ')
    print()
