for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        for i in range(1, (n//2) + 1):
            print(i + (n+1)//2, i, end=' ')
    else:
        for i in range(1, (n//2)+1):
            print(i, i+(n+2)//2, end=' ')
        if n%2 != 0:
            print((n+1)//2)
    print()