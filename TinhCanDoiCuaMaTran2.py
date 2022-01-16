n = int(input())
arr = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    arr.append(tmp)
k = int(input())
top, bottom = 0, 0
for i in range(0, n):
    for j in range(0, n - i - 1):
        top += arr[i][j]
    for j in range(n - i, n):
        bottom += arr[i][j]
hieu = abs(top - bottom)
res = 'YES' if hieu <= k else 'NO'
print(res)
print(hieu)
