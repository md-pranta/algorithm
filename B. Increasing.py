for _ in range(int(input())):
    n = int(input())
    if n == len(set(map(int, input().split()))):
        print('YES')
    else:
        print('NO')