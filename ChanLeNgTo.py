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
    check1, check2, check3 = True, True, True

    if not isPrime(sumDigits): check1 = False

    for i in range(0, len(digits)):
        if i % 2 == 0:
            if int(digits[i]) % 2 != 0:
                check2 = False
        else:
            if int(digits[i]) % 2 == 0:
                check3 = False
    if check1 and check2 and check3:
        print('YES')
    else:
        print('NO')
    # print(check1, check2, check3)

t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)