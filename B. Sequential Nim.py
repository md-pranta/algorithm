for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    one = 0
    for i in range(n):
        if a[i] == 1:
            one += 1
        else:
            break
    if one == n:
        if one & 1:
            print('First')
        else:
            print('Second')
        continue
    if not one & 1:
        print('First')
    else:
        print('Second')
