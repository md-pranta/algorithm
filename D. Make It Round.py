for _ in range(int(input())):
    n, m = map(int, input().split())
    tempn = n
    count2 = count5 = 0
    while tempn % 2 == 0:
        count2 += 1
        tempn //= 2
    while tempn % 5 == 0:
        count5 += 1
        tempn //= 5
    value = 1
    if count5 > count2:
        gap = count5 - count2
        while gap:
            if value * 2 <= m:
                value *= 2
            else:
                break
            gap -= 1
    else:
        gap = count2 - count5
        while gap:
            if value * 5 <= m:
                value *= 5
            else:
                break
            gap -= 1
    while True:
        if value * 10 <= m:
            value *= 10
        else:
             break
    value = m // value * value
    print(n * value)

