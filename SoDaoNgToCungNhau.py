def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def solve(s):
    a = int(s)
    b = int(s[::-1])
    if gcd(a, b) == 1:
        print('YES')
    else:
        print('NO')


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)