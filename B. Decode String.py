for _ in range(int(input())):
    n = int(input())
    s = input()

    ans = ''
    i = n-1
    while i >= 0:
        if s[i] != '0':
            ans += chr(int(s[i:i+1]) + 96)
            i -= 1
        else:
            ans += chr(int(s[i-2:i]) + 96)
            i -= 3
    print(ans[::-1])