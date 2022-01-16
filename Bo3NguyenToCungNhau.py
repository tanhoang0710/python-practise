def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def solve(l, r):
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            for k in range(j + 1, r + 1):
                if gcd(i, j) == 1 and gcd(i, k) == 1 and gcd(j, k) == 1:
                    print(f'({i}, {j}, {k})')


[l, r] = [int(x) for x in input().split()]
solve(l, r)
