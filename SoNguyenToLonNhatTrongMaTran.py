import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def solve(a): # gia su res la ele dau tien, duyet mang neu co ele nao la snt ma > res thi update res, cuoi
    #cung ktra lai res xem co la snt ko vi ele chua chac la snt
    res = a[0][0]
    for i in range(n):
        for j in range(m):
            if isPrime(a[i][j]) and a[i][j] > res:
                res = a[i][j]
                break
    if isPrime(res):
        print(res)
        for i in range(n):
            for j in range(m):
                if a[i][j] == res:
                    print(f'Vi tri [{i}][{j}]')
    else:
        print('NOT FOUND')


[n, m] = [int(x) for x in input().split()]
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
solve(a)
