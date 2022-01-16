def solve(a):
    tmp = []
    for ele in a:
        if ele not in tmp:
            tmp.append(ele)
            tmp.sort()
    res = []
    for ele in tmp:
        res.append([ele, a.count(ele) / len(a)])
    res = sorted(res, key=lambda l: l[1], reverse=True)
    for ele in res:
        for e in ele:
            print(e, end=' ')
        print()


t = int(input())
a = []
while t > 0:
    t -= 1
    s = input()
    a.extend(s.split())
solve(a)
