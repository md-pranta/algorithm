n = int(input())
a = n // 2 + 1
print(a)
for i in range(1, a + 1):
    print(1, i)
for j in range(2, (n - a) + 2):
    print(j, a)
