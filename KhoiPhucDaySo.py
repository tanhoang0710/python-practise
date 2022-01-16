a = []
n = int(input())
for i in range(n):
    a.append([int(x) for x in input().split()])
res = []
res.append((a[0][1] + a[0][2] - a[1][2]) // 2)
for i in range(1, n):
    res.append(a[0][i] - res[0])
for ele in res:
    print(ele, end=' ')