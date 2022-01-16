def gcd(a, b):
    t = 0
    while b > 0:
        t = a % b
        a = b
        b = t
    return a


t = int(input())
while t > 0:
    t -= 1
    a = int(input())
    b = int(input())
    print(gcd(a, b))