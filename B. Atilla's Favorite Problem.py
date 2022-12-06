for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = ord('a')
    for i in s:
        ans = max(ans, ord(i))
    print(ans-96)
