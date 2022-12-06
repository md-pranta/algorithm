for _ in range(int(input())):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    i = 1
    while s > 0:
        if i not in b:
            s -= i
            b.append(i)
        i += 1
    b.sort()
    x = (b[-1] * (b[-1] + 1)) // 2
    if x == sum(b) and s == 0:
        print('YES')
    else:
        print('NO')
