for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    odd = even = dif = 0
    if a[-1] & 1:
        odd += 1
    else:
        even += 1
    for i in range(n - 1):
        if a[i] & 1:
            odd += 1
        else:
            even += 1
        if a[i + 1] - a[i] == 1:
            dif += 1
    if odd % 2 != even % 2:
        print('NO')
    else:
        if not even & 1:
            print('YES')
        else:
            if dif:
                print('YES')
            else:
                print('NO')
