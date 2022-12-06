import itertools
import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    mini = math.inf
    count = 0
    ans = 0
    for i, j in itertools.product(range(n), range(m)):
        value = li[i][j]
        if value < 0:
            count += 1
        mini = min(mini, abs(value))
        ans += abs(value)
    if count & 1:
        print(ans - (2 * mini))
    else:
        print(ans)
