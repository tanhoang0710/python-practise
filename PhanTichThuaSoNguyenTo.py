import math

def solve(n):
    print('1', end='')
    for i in range(2, n + 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                n /= i
                dem += 1
            print(f' * {i}^{dem}', end='')
    print()


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    solve(n)
