import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n, a, b = M()
    s = S()
    if b < 0:
        part = sum(s[i] != s[i+1] for i in range(n-1))
        print(n * a + ((part + 1) // 2 + 1) * b)
    else:
        print((a * 1 + b)*n)
