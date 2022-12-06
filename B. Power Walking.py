for _ in range(int(input())):
    n = int(input())
    a = len(set(map(int, input().split())))
    for i in range(1, n + 1):
        if i > a:
            print(i, end=' ')
        else:
            print(a, end=' ')
    print()
