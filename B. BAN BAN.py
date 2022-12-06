for _ in range(int(input())):
    n = int(input())
    ans = n // 2 + n % 2
    print(ans)
    l, r = 1, 3 * n
    for _ in range(ans):
        print(l, r)
        l += 3
        r -= 3
