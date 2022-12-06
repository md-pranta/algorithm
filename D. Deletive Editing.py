"""
for _ in range(int(input())):
    a, b = input().split()
    check = ''
    for i in a[::-1]:
        if i in b and check.count(i) < b.count(i):
            check += i
    if check[::-1] == b:
        print('YES')
    else:
        print('NO')
"""

for _ in range(int(input())):
    a, b = input().split()
    x, b = len(b), f' {b}'
    for i in a[::-1]:
        if i == b[x]:
            x -= 1
        elif i in b[:x]:
            break
    if b[x] == ' ':
        print('YES')
        continue
    print('NO')
