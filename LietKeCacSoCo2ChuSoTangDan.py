def solve(s):
    s = s[::-1]
    for i in range(len(s) - 2, 0, -2):
        s = s[:i] + "," + s[i:]
    s = s[::-1]
    res = s.split(',')
    if len(res[-1]) < 2:
        res.remove(res[-1])
    res = list(dict.fromkeys(res))
    res = sorted(res)
    for ele in res:
        print(ele, end=' ')


s = input()
solve(s)