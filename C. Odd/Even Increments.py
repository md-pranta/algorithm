for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 2):
        if a[i] & 1 != a[i + 2] & 1:
            print('NO')
            break
    else:
        print('YES')
