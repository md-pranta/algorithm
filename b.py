for _ in range(int(input())):
    n = int(input())
    if n & 1:
        print('1 ' * n)
    else:
        for _ in range(n - 2):
            print(2, end=' ')
        print(3, 1)
