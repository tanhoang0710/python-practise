def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def solve(n, k):
    res = []
    for i in range(10**(k - 1), 10**k):
        if gcd(i, n) == 1:
            res.append(i)
    for i in range(len(res)):
        print(res[i], end=' ')
        tmp = int(len(res) / 10)
        for j in range(1, tmp + 1):
            if i == 10 * j - 1:
                print()


[n, k] = [int(x) for x in input().split()]
solve(n, k);