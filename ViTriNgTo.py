import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check1(s):
    for i in range(len(s)):
        if isPrime(i):
            if not isPrime(int(s[i])):
                return False
    return True

def check2(s):
    for i in range(len(s)):
        if not isPrime(i):
            if isPrime(int(s[i])):
                return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check2(s) and check1(s):
        print('YES')
    else:
        print('NO')