import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(a, n, m):
    for i in range(n):
        for j in range(m):
            if isPrime(a[i][j]):
                a[i][j] = 1
            else:
                a[i][j] = 0
    return a


[n, m] = [int(x) for x in input().split()]  #cach nhap 1 ma tran
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
res = solve(a, n, m)
for i in range(n):
    for j in range(m):
        print(res[i][j], end=' ')
    print()
