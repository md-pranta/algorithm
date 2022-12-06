import math
import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return sorted(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n = N()
    a = L()
    i = 1
    maxi = a[n-1]
    ans = 1
    while i < n:
        maxi = min(maxi, a[i] - a[i-1])
        if maxi < a[i]:
            break
        ans += 1
        i += 1
    print(ans)
