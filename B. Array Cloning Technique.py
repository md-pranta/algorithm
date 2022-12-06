for _ in range(int(input())):
    n = int(input())
    dic = {}
    for i in input().split():
        if dic.get(i, 0):
            dic[i] += 1
        else:
            dic[i] = 1
    most = max(dic.values())
    copies = n-most
    while most < n:
        copies += 1
        most *= 2
    print(copies)