for _ in range(int(input())):
    n = int(input())
    q = input()
    ans = 0
    for i in q[::-1]:
        if i == 'A':
            ans += 1
        else:
            ans -= 1
        if ans <= -1:
            print('No')
            break
    else:
        print('YES')


