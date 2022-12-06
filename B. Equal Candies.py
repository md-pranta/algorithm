for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    print(sum(num - m for num in a))