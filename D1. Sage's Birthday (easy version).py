n = int(input())
a = list(map(int, input().split()))
temp = sorted(a)
can_buy = n // 2 if n & 1 else n // 2 - 1
li = []
i = can_buy
print(can_buy)
can_buy -= 1
while i < n and can_buy >= 0:
    li.append(temp[i])
    i+= 1
    li.append(temp[can_buy])
    can_buy -= 1
while i < n:
    li.append(temp[i])
    i += 1
print(*li)
