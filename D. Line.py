for _ in range(int(input())):
    n = int(input())
    s = input()
    li = []
    total = 0
    for i in range(n):
        m = max(i, n - i - 1)
        if s[i] == 'L':
            if i < m:
                li.append(m-i)
            else:
                li.append(0)
            total += i

        else:
            if n - i - 1 < m:
                li.append(m-n+i+1)
            else:
                li.append(0)
            total += n - i - 1
    li.sort(reverse=True)
    for j in range(n):
        total += li[j]
        print(total,end=' ')
    print()
