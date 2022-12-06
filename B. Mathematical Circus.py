for _ in range(int(input())):
    n, k = map(int, input().split())
    if not k % 4:
        print('NO')
    else:
        print('YES')
        for i in range(1,n+1,2):
            if ((i + k) * (i+1)) % 4:
                print(i+1, i)
            else:
                print(i, i+1)
