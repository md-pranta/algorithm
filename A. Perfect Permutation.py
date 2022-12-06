for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    elif n & 1:
        print(1, end=' ')
        for i in range(2, n + 1, 2):
            print(i + 1, i, end=' ')
    else:
        for i in range(1, n + 1, 2):
            print(i + 1, i, end=' ')
