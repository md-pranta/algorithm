n = int(input())
#
counter = 0
while n != 0:
    rsb = n & -n
    n -= rsb
    counter += 1

print(counter)