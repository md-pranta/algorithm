for _ in range(int(input())):
    a = sorted(map(int, input().split()))
    if a[0] + a[1] >= a[2]:
        print(sum(a)//2)
    else:
        print(a[0] + a[1])