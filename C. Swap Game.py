for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] <= min(a[1::]):
        print('Bob')
    else:
        print('Alice')