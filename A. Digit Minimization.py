from math import inf
for _ in range(int(input())):
    n = input()
    if len(n) == 2:
        print(n[-1])
    else:
        small = inf
        for i in n:
            small = min(small, int(i))
        print(small)