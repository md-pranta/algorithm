for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x = a - 1
    if b < c:
        y = (c - b)*2
        if b == 2:
            y += 1
    else:
        y = b - c
    if a == 1:
        print(1)
    elif x == y:
        print(3)
    elif x < y:
        print(1)
    elif x > y:
        print(2)

