import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
array = list(map(int, input().split()))
res = []
for i in range(0, n):
    count = 0
    if isPrime(array[i]):
        count = array.count(array[i])
        pair = str(array[i]) + " " + str(count)
        res.append(pair)

res = list(dict.fromkeys(res))
for i in range(0, len(res)):
    print(res[i])
