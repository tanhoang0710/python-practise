def check(n):
    n = str(n)
    if len(n) < 2:
        return False
    tmp = n[::-1]
    return n == tmp


[n, m] = [int(x) for x in input().split()]
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
res = a[0][0]
for i in range(n):
    for j in range(m):
        if check(a[i][j]) and a[i][j] > res:
            res = a[i][j]
            break
if check(res):
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f'Vi tri [{i}][{j}]')
else:
    print('NOT FOUND')
