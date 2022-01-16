import math


def gcd(a, b):
    t = 0
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def tongCS(n):
    t = 0
    while n > 0:
        t += n % 10
        n //= 10
    return t


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    [a, b] = [int(x) for x in input().split()]
    if isPrime(tongCS(gcd(a, b))):
        print('YES')
    else:
        print('NO')
    # print(tongCS(a), tongCS(b))