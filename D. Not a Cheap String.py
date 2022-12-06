for _ in range(int(input())):
    s = input()
    n = int(input())

    li = []
    total_value = 0
    for i in range(len(s)):
        total_value += ord(s[i]) - 96
        li.append([s[i], i])

    li = sorted(li)
    while li and n < total_value:
        total_value -= ord(li[-1][0]) - 96
        li.pop()

    li.sort(key=lambda x: x[1])

    for a in li:
        print(a[0], end='')
    print()
