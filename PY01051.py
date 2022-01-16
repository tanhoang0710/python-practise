def solve(n):
    s = str(n)
    tong = 0
    if len(s) < 2:
        return False
    for i in range(len(s)):
        tong += int(s[i])
    ns = str(tong)
    return ns == ns[::-1] and len(ns) > 1


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if solve(n):
        print("YES")
    else:
        print('NO')