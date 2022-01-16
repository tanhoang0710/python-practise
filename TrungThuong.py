

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = []
    res = []
    for i in range(n):
        ele = int(input())
        a.append(ele)
    for ele in a:
        if ele not in res:
            res.append(ele)
    dem = a.count(res[0])
    ans = a[0]
    for ele in res:
        if a.count(ele) >= dem:
            if ele < ans:
                dem = a.count(ele)
                ans = ele
    print(ans)
