import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return sorted(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n = N()
    a = L()

    if n & 1 or a[0] == a[-1]:
        print('NO')
    else:
        li = []
        for i in range(n // 2):
            li.extend((a[i], a[i + n // 2]))
        for j in range(n):
            if not (li[j - 1] < li[j] > li[j + 1 - n]) and \
                    not (li[j - 1] > li[j] < li[j + 1 - n]):
                print('NO')
                break

        else:
            print('YES')
            print(*li)


