for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = i = a.index(min(a))
    x = 1
    while i < n-1:
        if a[i] > a[i+1]:
            x = 0
            print('NO')
            break
        i += 1
    if x:
        while m > 0:
            if a[m-1] < a[m]:
                print('NO')
                break
            m -= 1
        else:
            print('YES')