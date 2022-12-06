for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1):
        if a[i] in a[i+1::]:
            print(i+1, n)
            break
    else:
        print(1, n)
