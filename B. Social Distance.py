for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))
    if n >= m:
        print('NO')
    else:
        total_seat = 2 * a[0] + 1 - min(a[0], a[-1])
        for i in range(1, n):
            total_seat += 2 * a[i] + 1 - min(a[i - 1], a[i])
            if total_seat > m:
                print('NO')
                break
        else:
            print('YES')
