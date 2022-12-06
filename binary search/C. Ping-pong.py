for _ in range(int(input())):
    s = input()
    if not len(s)&1 and s[0] != ')' and s[-1] != '(':
        print('YES')
    else:
        print('NO')
