import sys


def N(): return int(sys.stdin.buffer.readline())


def S(): return sys.stdin.buffer.readline().rstrip().decode()


def solve(x, a):
    if 3 * a.count('M') != x:
        return 'NO'
    t = 0
    for i in a:
        if i == 'T':
            t += 1
        else:
            t -= 1
        if t < 0:
            return 'NO'
    t = 0
    for j in a[::-1]:
        if j == 'T':
            t += 1
        else:
            t -= 1
        if t < 0:
            return 'NO'
    return 'YES'


for _ in range(N()):
    n = N()
    s = S()
    print(solve(n, s))
