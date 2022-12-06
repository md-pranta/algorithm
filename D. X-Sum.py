import itertools
for _ in range(int(input())):
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    maxi = 0
    for i, j in itertools.product(range(n), range(m)):
        temp = 0
        # upper secondary diagonal
        point_ro = i - 1
        point_co = j + 1
        while point_ro >= 0 and point_co < m:
            temp += li[point_ro][point_co]
            point_co += 1
            point_ro -= 1
        # lower secondary diagonal
        point_ro = i + 1
        point_co = j - 1
        while point_ro < n and point_co >= 0:
            temp += li[point_ro][point_co]
            point_ro += 1
            point_co -= 1
        # upper principal diagonal
        point_ro = i+1
        point_co = j+1
        while point_ro < n and point_co < m:
            temp += li[point_ro][point_co]
            point_ro += 1
            point_co += 1
        # lower principal diagonal
        point_ro = i - 1
        point_co = j - 1
        while point_ro >= 0 and point_co >= 0:
            temp += li[point_ro][point_co]
            point_ro -= 1
            point_co -= 1

        # placed in bishop
        temp += li[i][j]
        maxi = max(maxi, temp)
    print(maxi)