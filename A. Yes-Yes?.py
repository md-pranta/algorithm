for _ in range(int(input())):
    s = input()
    if 'Y' in s:
        y = s.index('Y')
    else:
        if s in ['s', 'e', 'es']:
            print('Yes')
            continue
        print('NO')
        continue
    x = s[:y]
    if x not in ['es', 's', '']:
        print('NO')
        continue
    cur = 'e'
    for i in range(y+1,len(s)):
        if s[i] == cur:
            if cur == 'Y':
                cur = 'e'
            elif cur == 'e':
                cur = 's'
            else:
                cur = 'Y'
        else:
            print('NO')
            break
    else:
        print('YES')