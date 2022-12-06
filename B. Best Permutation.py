for _ in range(int(input())):
    n = int(input())
    if n & 1:
        for i in range(n-2, 3, -1):
            print(i, end=' ')
        print(1, 2, 3, n - 1, n)
    else:
        for i in range(n - 2, 0, -1):
            print(i, end=' ')
        print(n - 1, n)
