for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c0 = c1 = c2 = 0
    for num in a:
        if num % 3 == 0:
            c0 += 1
        elif num % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    print(max((c1 - c0), (c2-c1), (c0 - c2)))