for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    first = False
    for i in range(n-1):
        if a[i]:
            count += a[i]
            first = True
        elif first:
            count += 1
    print(count)
