for _ in range(int(input())):
    li = sorted(map(int, input().split()))
    if li[0] + li[1] == li[2]:
        print('YES')
    else:
        print('NO')