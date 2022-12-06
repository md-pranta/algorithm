import math
import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    a, b = M()

    z = a * b << 2
    if b == 1:
        print('NO')
    else:
        print('YES')
        print(a, z - a, z)