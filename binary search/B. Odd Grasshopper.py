for _ in range(int(input())):
    x, n = map(int, input().split())
    same_at = n // 4
    for i in range((same_at * 4) + 1, (same_at * 4) + n % 4 + 1):
        if x & 1:
            x += i
        else:
            x -= i
    print(x)
