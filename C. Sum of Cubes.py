import math

for _ in range(int(input())):
    x = int(input())
    a = x ** (1 / 3)
    for i in range(1, math.ceil(a)):
        b = x - math.pow(i,3)
        b = b ** (1/3)
        if pow(i, 3) + pow(int(b), 3) == x:
            print('YES')
            break
    else:
        print('NO')
