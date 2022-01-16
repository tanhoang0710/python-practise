import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(s):
    for i in range(len(s) - 1, 0, -1):
        s = s[:i] + "," + s[i:]
    digits = s.split(',')
    sumDigits = 0
    for digit in digits:
        sumDigits += int(digit)

    if isPrime(sumDigits):
        print('YES')
    else:
        print('NO')
    # print(str(sumDigits))
    # print(str(sumDigits)[::-1])


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)