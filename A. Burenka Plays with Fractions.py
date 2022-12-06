for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    left = a * d
    right = c * b
    if left == right:
        print(0)
    elif not left or not right or not (left % right) or not (right % left):
        print(1)
    else:
        print(2)
