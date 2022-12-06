import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    a, b = M()
    v = [a - 1, 1, a, 0]
    c = v[(a - 1) % 4]
    if c == b:
        print(a)
    elif c ^ b == a:
        print(a + 2)
    else:
        print(a + 1)
