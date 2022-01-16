def solve(a):
    tmp = []
    for ele in a:
        tmp.append(ele.lower())
    res = set(tmp)
    print(*res)


t = int(input())
a = []
while t > 0:
    t -= 1
    s = input()
    a.append(s)
solve(a)
