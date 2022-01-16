def solve(a):
    tmp = []
    for ele in a:
        if ele not in tmp:
            tmp.append(ele)
            tmp.sort()
    res = []
    for ele in tmp:
        res.append([ele, a.count(ele)])
    res = sorted(res, key=lambda l: l[1], reverse=True)
    print(res[1][0], end=' ')
    for i in range(2, len(res)):
        if res[i][1] == res[1][1]:
            print(res[i][0], end=' ')


t = int(input())
a = []
while t > 0:
    t -= 1
    s = input()
    a.extend(s.split())
solve(a)