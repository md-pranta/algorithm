import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n = N()
    number = N()
    if str(number)[0] == '9':
        print(int('1'*(n + 1)) - number)
    else:
        print(int('9' * n) - number)