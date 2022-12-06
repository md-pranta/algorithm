for _ in range(int(input())):
    n, m = map(int, input().split())
    s = ['B'for _ in range(m)]
    a = list(map(int, input().split()))
    for num in a:
        suf = m+1-num
        if num <= suf and s[num - 1] != 'A' or num > suf and s[suf - 1] == 'A':
            s[num-1] = 'A'
        else:
            s[suf - 1] = 'A'
    for c in s:
        print(c,end='')
    print()
