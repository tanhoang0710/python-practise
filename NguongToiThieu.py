def solve(s, k):
    s = s[::-1]
    for i in range(len(s) - 2, 0, -2):
        s = s[:i] + "," + s[i:]
    s = s[::-1]
    res = s.split(',')
    if len(res[-1]) < 2:
        res.remove(res[-1])
    countArr = []
    tmp = list(dict.fromkeys(res))  # tao 1 array phu de dem  ma ko bi lap
    for ele in tmp:
        if res.count(ele) >= k:
            countArr.append([ele, res.count(ele)])
    if len(countArr) > 0:
        countArr = sorted(countArr)
        for i in countArr:
            for j in i:
                print(j, end=' ')
            print()
    else:
        print('NOT FOUND')


s = input()
k = int(input())
solve(s,k)