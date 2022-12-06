def check(number, n):
    if str(n) in str(number):
        return 'Yes'
    if number >= 10 * n:
        return 'Yes'
    for _ in range(1, 11):
        number -= n
        if number < n:
            return 'No'
        if str(n) in str(number):
            return 'Yes'


for _ in range(int(input())):
    q, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in a:
        print(check(i, d))
