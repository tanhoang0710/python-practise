import math

def isPrime(n):
    if n < 2:
        return False
    sqrt = int(math.sqrt(n)) + 1
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True

# tim day 1000 so ngTo dau tien va lam theo cong thuc
def solve(n, x):
    primeArr = []
    count = 0
    m = 2
    while count < 1000:
        if isPrime(m):
            primeArr.append(m)
            count += 1
        m += 1

    res = [x]
    for i in range(1, n+1):
        res.append(res[i - 1] + primeArr[i - 1])
    for ele in res:
        print(ele, end=' ')
    # print(len(primeArr))
    # print(primeArr)


[n, x] = [int(x) for x in input().split()]
solve(n, x)
#2, 3, 5, 7, 11, 13, 17, 19, 23, 29
