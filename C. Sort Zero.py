for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        if a[i] in dic:
            x = dic.get(a[i]).append(i)
            dic[a[i]] = x
        else:
            dic[a[i]] = list(int(i))

    print(dic)
