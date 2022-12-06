for _ in range(int(input())):
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    z = abs(r - l)
    y = abs(a) + x
    if (not l <= b <= r or a - x < l and a + x > r) and a != b:
        print(-1)
    elif a == b:
        print(0)
    else:
        m = abs(r - a)
        n = abs(a - l)
        if abs(b - a) >= x:
            print(1)
        elif m >= x and abs(r - b) >= x:
            print(2)
        elif n >= x and abs(b - l) >= x:
            print(2)
        elif abs(b - l) >= x or abs(r - b) >= x:
            print(3)
        else:
            print(-1)
