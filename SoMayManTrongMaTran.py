[n, m] = [int(x) for x in input().split()]
a = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    a.append(tmp)
#Tim max min va duyet array roi tim
minNum, maxNum, res = a[0][0], a[0][0], a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > maxNum:
            maxNum = a[i][j]
        elif a[i][j] < minNum:
            minNum = a[i][j]
for i in range(n):
    for j in range(m):
        if a[i][j] == maxNum - minNum:
            res = a[i][j]
            break
if res == maxNum - minNum:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f'Vi tri [{i}][{j}]')
else:
    print('NOT FOUND')
