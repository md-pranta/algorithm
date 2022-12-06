for _ in range(int(input())):
    n = int(input())
    if n == 3:
        print(-1)
    elif n == 2:
        print(2, 1)
    else:
        print(n, n - 1, end=' ')
        for i in range(1, n - 1):
            print(i, end=' ')
        print()
