for _ in range(int(input())):
    n = input()

    fi = (ord(n[0]) - 97)*25
    se = ord(n[-1])-96
    if ord(n[0]) < ord(n[-1]):
        se -= 1
    print(fi+se)


