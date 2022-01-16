import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def solve(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return isPrime(count)


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if solve(n):
        print('YES')
    else:
        print('NO')