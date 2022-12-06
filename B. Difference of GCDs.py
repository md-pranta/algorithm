from math import ceil
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    li = []
    for i in range(1, n+1):
        number = ceil(l/i) * i
        if number <= r:
            li.append(number)
        else:
            print('NO')
            break
    else:
        print('YES')
        print(*li)