from sys import stdin, stdout


def solve(n, x):
    if n % x != 0: return -1
    d = {i: i for i in range(1, n + 1)}
    i = 1
    while i < n:
        # print(" ".join(map(str, d.values())))
        if x > n: return -1
        d[i] = x
        i = x
        if x == n: break
        for j in range(2, 20000):
            if n % (x * j) == 0:
                x = x * j
                break
            if x * j > n: return -1
        # print(x)
    d[n] = 1
    return " ".join(map(str, d.values()))


for _ in range(int(stdin.readline().strip())):
    n, x = map(int, stdin.readline().strip().split())
    ans = solve(n, x)
    stdout.write(f"{ans}\n")
