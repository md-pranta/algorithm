for _ in range(int(input())):
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    maxi = max(a)
    mex = 0
    while mex in a:
        mex += 1
    if k == 0:
        print(n)
    elif mex > maxi:
        print(n + k)
    elif (mex + maxi + 1)//2 in a:
        print(n)
    else:
        print(n + 1)