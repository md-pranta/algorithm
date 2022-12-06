import math
import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


def check(a):
    b = int(math.sqrt(a))
    return b**2 == a


for _ in range(N()):
    n = N()
    if n == 2:
        print(-1)
    else:
        if n == 1:
            print(1)
            continue
        x = 1
        for _ in range(n):
            for _ in range(n):
                if x > n ** 2:
                    x = 2
                print(x,end=' ')
                x += 2
            print()