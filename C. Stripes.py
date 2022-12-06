for _ in range(int(input())):
    li = []
    print()
    for _ in range(8):
        a = input()
        x = list(a)
        li.append(x)

    for i in range(8):
        red = sum(li[i][j] == 'R' for j in range(8))
        if red == 8:
            print('R')
            break
    else:
        print('B')
