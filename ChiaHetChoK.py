[a, k, n] = [int(x) for x in input().split()]
res = []
x = 1
# tim boi cua k
while k * x - a <= n - a:
    if k * x - a > 0:
        res.append(k * x - a)
    x += 1

if len(res) > 0:
    for x in res:
        print(x, end=' ')
else:
    print(-1)
