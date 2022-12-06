for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    c = 0
    maxi = l[0]
    mini = l[0]
    for i in l[1:]:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
        if maxi - x > mini + x:
            c += 1
            maxi = mini = i
    print(c)
