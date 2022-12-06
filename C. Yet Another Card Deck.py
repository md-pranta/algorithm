import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


def solve(l, ql):
    res = []
    used = []
    position = []
    count = 0
    for i in ql:
        if i not in used:
            p = l.index(i)
            final = p + 1
            for item in position:
                if item > p:
                    final += 1
            res.append(final)
            used.append(i)
            position.append(p)
            count += 1
        else:
            final = used.index(i)
            res.append(count - final)
            used.append(used.pop(final))
    return res


n, q = M()
li = L()
queries = L()
print(*solve(li, queries))
