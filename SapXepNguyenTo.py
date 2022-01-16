import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(x) for x in input().split()]
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if isPrime(a[j]) and isPrime(a[i]):
            if a[i] > a[j]:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
for ele in a:
    print(ele, end=' ')
