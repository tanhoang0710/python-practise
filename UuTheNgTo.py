import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    prime = 0
    notPrime = 0
    for c in s:
        if isPrime(int(c)):
            prime += 1
        else:
            notPrime += 1
    return prime > notPrime


def solve(s):
    if isPrime(len(s)) and check(s):
        print('YES')
    else:
        print('NO')


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)