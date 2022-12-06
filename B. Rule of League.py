for _ in range(int(input())):
    n, x, y = map(int, input().split())
    if (x and y) or (x == 0 and y == 0):
        print(-1)
    elif (n - 1) % max(x, y):
        print(-1)
    else:
        player = 1
        c = 0
        for i in range(1, n):
            print(player,end=' ')
            c += 1
            if c == max(x, y):
                player = i + 2
                c = 0
        print()
