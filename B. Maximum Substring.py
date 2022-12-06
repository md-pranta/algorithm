for _ in range(int(input())):
    n = int(input())
    s = input()
    one = 0
    zero = 0
    temp = 0
    count = 1
    if s[0] == '1':
        one += 1
    else:
        zero += 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
        else:
            temp = max(count, temp)
            count = 1
        if s[i] == '1':
            one += 1
        else:
            zero += 1
    temp = max(temp, count)
    if temp * temp > one * zero:
        print(temp ** 2)
    else:
        print(one * zero)
