import math

def gcd(a, b):
    t = 0
    while b > 0:
        t = a % b
        a = b
        b = t
    return a


def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def solve(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    if isPrime(count):
        return True
    return False


t = int(input())
while t > 0:
    n = int(input())
    if solve(n):
        print("YES")
    else:
        print('NO')
    t -= 1
