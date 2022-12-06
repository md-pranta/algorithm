for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    for i in range(n):
        if a[i] != b[i] and a[i] + 1 != b[i]:
            print('NO')
            break
    else:
        print('YES')
