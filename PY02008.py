import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# tao 1 mang luu 1000 so nguyen to dau tien roi push n so nguyen to vao bang ket qua 

def solve(n, x):
    res = [x]
    a = []
    count = 0
    m = 2
    while count < 1000:
        if isPrime(m):
            a.append(m)
            count += 1
        m += 1
    for i in range(1, n + 1):
        res.append(res[i - 1] + a[i - 1])
    for ele in res:
        print(ele, end=' ')


[n, x] = [int(x) for x in input().split()]
solve(n, x)