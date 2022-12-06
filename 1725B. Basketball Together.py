n, d = map(int, input().split())
p = sorted(map(int, input().split()), reverse=True)
ans = 0
for num in p:
    if n >= d // num + 1:
        n -= d // num + 1
        ans += 1
    else:
        break
print(ans)
