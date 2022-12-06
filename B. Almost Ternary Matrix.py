s = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
for _ in range(int(input())):
    n, m = map(int, input().split())

    for i in range(n):
        for j in range(m):
            print(s[i % 4][j % 4], end=' ')
        print()
