import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('1' + '0' * (a - 1), '1' * (b - c + 1) + '0' * (c - 1))
