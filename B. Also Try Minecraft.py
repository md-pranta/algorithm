n, m = map(int, input().split())
a = list(map(int, input().split()))

suffix, prefix = [0], [0]
for i in range(n-1):
    if a[i] > a[i+1]:
        prefix.append(a[i] - a[i+1])
        suffix.append(0)
    else:
        prefix.append(0)
        suffix.append(a[i+1] - a[i])
    prefix[i+1] += prefix[i]
    suffix[i+1] += suffix[i]


for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(prefix[t-1] - prefix[s-1])
    else:
        print(suffix[s-1] - suffix[t-1])
