import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solve(a):
    b = []
    for ele in a:
        if ele not in b and isPrime(ele):
            b.append(ele)
    count = 0
    for ele in b:
        count = 0
        for e in a:
            if e == ele:
                count += 1
        print(ele, count)


n = int(input())
a = [int(x) for x in input().split()]
solve(a)
