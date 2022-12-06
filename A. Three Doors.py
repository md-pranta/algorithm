for _ in range(int(input())):
    x = int(input())
    a = list(map(int, input().split()))
    if a[x-1] != 0:
        x = a[x-1]
        if a[x-1] != 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')