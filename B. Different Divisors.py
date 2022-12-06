def isPrime(number):
    if number <= 1:
        return False
    return all(number % divisor for divisor in range(3, int(number ** 0.5) + 2, 2))


def getPrime(n):
    if n == 2:
        return n
    if n % 2 == 0:
        n += 1
    while True:
        if isPrime(n):
            return n
        n += 2


for _ in range(int(input())):
    d = int(input())
    p = getPrime(d + 1)
    q = getPrime(p + d)
    print(p * q)
