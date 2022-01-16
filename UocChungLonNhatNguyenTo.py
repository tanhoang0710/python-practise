import math


def isPrime(n):
    if n < 2 : return False
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


def sumDigit(n):
    sum = 0
    while n > 0:
        sum += int(n % 10)
        n /= 10
    return int(sum)


t = int(input())
while t > 0:
    t -= 1
    inp = [int(x) for x in input().split()]

    a = inp[0]
    b = inp[1]
    GCD = gcd(a, b)
    res = sumDigit(GCD)

    if isPrime(res):
        print('YES')
    else:
        print('NO')
    # print(GCD)