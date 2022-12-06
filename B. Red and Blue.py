for _ in range(int(input())):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    r_max = b_max = 0
    temp = 0
    for i in r:
        temp += i
        r_max = max(r_max, temp)
    tem = 0
    for j in b:
        tem += j
        b_max = max(b_max, tem)
    print(r_max+b_max)