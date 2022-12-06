def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


for _ in range(int(input())):
    n = int(input())
    li = []
    if n == 1:
        print(1)
        continue
    else:
        for a in range(n, 1, -2):
            li.extend((a - 1, a))
    if n & 1:
        li.append(1)
    for i in range(n - 1, -1, -1):
        print(li[i], end=' ')
