import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(b):
    for i in range(len(b)):
        sum1 = 0
        sum2 = 0
        for j in range(len(b)):
            if j <= i:
                sum1 += b[j]
            else:
                sum2 += b[j]
        if isPrime(sum1) and isPrime(sum2):
            return i
    return -1


n = int(input())
a = [int(x) for x in input().split()]
b = []
for ele in a:
    if ele not in b:
        b.append(ele)
if solve(b) != -1:
    print(solve(b))
else:
    print('NOT FOUND')

