for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for number in a:
        if number % a[0]:
            print('NO')
            break
    else:
        print('YES')
