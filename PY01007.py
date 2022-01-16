def solve(n, x, m):
    tong = n
    nam = 0
    while tong < m:
        nam += 1
        tong += tong * (x / 100)
    return nam


t = int(input())
while t > 0:
    t -= 1
    [n, x, m] = [float(x) for x in input().split()]
    print(solve(n, x, m))
