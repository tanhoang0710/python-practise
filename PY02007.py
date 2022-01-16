def flat(a):
    res = []
    for ele in a:
        for e in ele:
            res.append(e)
    return res


test = 10
a = []
while test > 0:
    tmp = input().split()
    test -= len(tmp)
    a.append(tmp)
a = flat(a)
res = []
for ele in a:
    res.append(int(ele) % 42)
print(len(set(res)))
