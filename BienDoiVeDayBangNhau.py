# Cach lam: in ra tong do chenh lech cac so voi so o giua sau khi da sap xep
def solve(a):
    tong = 0
    res = 1e9
    num = 0
    for i in range(len(a)):
        tong = 0
        for j in range(len(a)):
            tong += abs(a[j] - a[i])
        if tong < res:
            res = tong
            num = i
    print(res, a[num])


n = int(input())
a = [int(x) for x in input().split()]
solve(a)
# 1 1 2 2