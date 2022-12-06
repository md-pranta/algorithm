for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    total_sum = 0
    for i in range(n-1):
        if abs(a[i] - a[i+1])+abs(b[i] - b[i+1]) < abs(a[i] - b[i+1]) + abs(b[i]-a[i+1]):
            total_sum += abs(a[i] - a[i+1])+abs(b[i] - b[i+1])
        else:
            total_sum += abs(a[i] - b[i+1]) + abs(b[i]-a[i+1])
    print(total_sum)
