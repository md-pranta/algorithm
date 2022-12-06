import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


for _ in range(N()):
    n, k = M()
    a = L()
    b = sorted(a)
    dic = {b[j]: j for j in range(n)}
    subarray = 1 + sum(dic[a[i]]+1 != dic[a[i+1]] for i in range(n-1))
    if k < subarray:
        print('NO')
    else:
        print('YES')