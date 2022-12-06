import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")


def II(): return int(sys.stdin.buffer.readline())


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))


def LI1(): return list(map(int1, sys.stdin.buffer.readline().split()))


def LLI(rows_number): return [LI() for _ in range(rows_number)]


def LLI1(rows_number): return [LI1() for _ in range(rows_number)]


def BI(): return sys.stdin.buffer.readline().rstrip()


def SI(): return sys.stdin.buffer.readline().rstrip().decode()


# dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dij = [(0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
inf = 10 ** 16
# md = 998244353
md = 10 ** 9 + 7


def ok():
    m = s.count("M")
    if m * 3 != n: return False

    now = 0
    for c in s:
        if c == "T":
            now += 1
        else:
            now -= 1
        if now < 0: return False
    now = 0
    for c in s[::-1]:
        if c == "T":
            now += 1
        else:
            now -= 1
        if now < 0: return False
    return True


for _ in range(II()):
    n = II()
    s = SI()
    print("YES" if ok() else "NO")
