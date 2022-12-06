for _ in range(int(input())):
    s = input()
    n = remove = len(s)
    for i in range(n - 1, -1, -1):
        if s[i] == '5':
            temp = n - 1 - i
            for j in range(i - 1, -1, -1):
                if s[j] in ['2', '7']:
                    temp += i - 1 - j
                    remove = min(remove, temp)
                    break
        elif s[i] == '0':
            temp = n - 1 - i
            for j in range(i - 1, -1, -1):
                if s[j] in ['0', '5']:
                    temp += i - 1 - j
                    remove = min(remove, temp)
                    break
    print(remove)
