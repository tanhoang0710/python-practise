def solve(n, p):
    res = 0
    tmp = 0
    while n > 0:
        tmp = int(n / p)
        res += tmp
        n /= p
    return res

t = int(input())
while t > 0:
    t -= 1
    inp = [int(x) for x in input().split()]
    n = inp[0]
    p = inp[1]
    res = solve(n, p)
    print(res)

