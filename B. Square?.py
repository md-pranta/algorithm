for _ in range(int(input())):
    a, b = map(int, input().split())
    a1, b1 = map(int, input().split())

    if max(a, b) == max(a1, b1):
        if min(a, b) + min(a1, b1) == max(a, b):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')