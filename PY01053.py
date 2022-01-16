def solve(n):
    s = str(n)
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong % 3 == 0


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if solve(n):
        print("YES")
    else:
        print('NO')

