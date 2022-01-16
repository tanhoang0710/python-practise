def solve(a):
    tmp = []
    for i in range(len(a) - 1):
        if abs(a[i] + a[i + 1]) == abs(a[i]) + abs(a[i + 1]):
            tmp.append(a[i])
            tmp.append(a[i + 1])
    if len(tmp) == 0:
        print(0)
    else:
        print(len(tmp) / 2, tmp[-2], tmp[-1])


n = int(input())
a = [int(x) for x in input().split()]
solve(a)