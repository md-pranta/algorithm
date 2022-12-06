for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    print(a[n-1]+a[n-2] - a[0] - a[1])