import math


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(n):
    s = str(n)
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return isprime(tong)


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if solve(n):
        print('YES')
    else:
        print("NO")