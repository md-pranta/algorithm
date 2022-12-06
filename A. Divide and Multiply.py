for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    divisor = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] //= 2
            divisor += 1
    print(max(a) * 2 ** divisor + sum(a) - max(a))