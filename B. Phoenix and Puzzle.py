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
    if n & 1:
        print('NO')
        continue
    n >>= 1
    if check(n):
        print('YES')
        continue
    if n & 1:
        print('NO')
        continue
    n >>= 1
    if check(n):
        print('YES')
        continue
    print('NO')


