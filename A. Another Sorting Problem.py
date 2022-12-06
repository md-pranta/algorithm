import sys
def N(): return int(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def L(): return list(map(int, sys.stdin.readline().split()))
def M(): return map(int, sys.stdin.readline().split())


n, m = M()
dic = {}
li = []
for i in range(n):
    s = S()
    dic[s] = i
    li.append(s)
for j in range(m-1, -1, -1):
    if j & 1:
        li.sort(key=lambda x: x[j], reverse=True)
    else:
        li.sort(key=lambda x: x[j])
for k in li:
    print(dic[k] + 1, end=' ')
print()