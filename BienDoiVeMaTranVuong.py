s = input()
n = int(s.split()[0])
m = int(s.split()[1])

a = []
for i in range(n):
    a.append([int(x) for x in input().split()])

if n != m:
    b = []
    if n > m:
        count = 0
        diff = n - m
        tmp = []
        for i in range(0, diff + 1, 2):
            tmp.append(i + 1)
        for i in range(n):
            if i + 1 not in tmp:
                b.append(a[i])
                count += 1
            if count == m:
                break
    if m > n:
        count = 0
        diff = m - n
        tmp = []
        for i in range(1, diff + 2, 2):
            tmp.append(i + 1)
        for i in range(n):
            arr = []
            count = 0
            for j in range(m):
                if j + 1 not in tmp:
                    arr.append(a[i][j])
                    count += 1
                    if count == n:
                        break
            b.append(arr)

    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], end=' ')
        print()

else:
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
