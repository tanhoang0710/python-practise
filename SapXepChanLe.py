def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(int(j))
    return new_list


n = int(input())
m = n
a = []
while n > 0:
    data = input()
    base = data.split()
    n -= len(base)
    a.append(base)
a = flatten(a)
for i in range(0, m - 1):
    for j in range(i + 1, m):
        if a[i] > a[j] and a[i] % 2 == 0 and a[j] % 2 == 0:
            a[i], a[j] = a[j], a[i]
        if a[i] < a[j] and a[i] % 2 != 0 and a[j] % 2 != 0:
            a[i], a[j] = a[j], a[i]

for ele in a:
    print(ele, end=' ')
