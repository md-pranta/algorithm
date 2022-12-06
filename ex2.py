import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
w = []
for i in range(n):
    s = input()[:-1]
    d[s] = i
    w.append(s)

for i in range(m-1,-1,-1):
    if i % 2:
        w.sort(key=lambda x:x[i], reverse=True)
    else:
        w.sort(key=lambda x:x[i])

for i in w:
    print(d[i] + 1, end=' ')