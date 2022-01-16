def gcd(a, b):
    tmp = 0
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = []
for i in range(n-1):
    for j in range(i+1, n, 1):
        if gcd(arr[i], arr[j]) == 1:
            res.append([arr[i], arr[j]])

for element in res:
    print(element[0], element[1])

