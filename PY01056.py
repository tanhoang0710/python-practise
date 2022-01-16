import math


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check1(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return isprime(tong)


def check2(s):
    for i in range(0, len(s)):
        if i % 2 != 0:
            if int(s[i]) % 2 == 0:
                return False
    return True


def check3(s):
    for i in range(0, len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0:
                return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check1(s) and check2(s) and check3(s):
        print("YES")
    else:
        print('NO')
