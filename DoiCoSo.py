def solve(n, b):
    res = ""
    tmp = n
    while tmp > 0:
        du = tmp % b
        if du >= 10: res += str(chr(du + 55))
        else:
            res += str(du)
        tmp = tmp // b
    print(res[::-1])


t = int(input())
while t > 0:
    s = [int(x) for x in input().split()]
    n = int(s[0])
    b = int(s[1])
    solve(n, b)
    t -= 1
