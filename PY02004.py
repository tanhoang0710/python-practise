def solve(a):
    res = 0
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            res += 1
    return res


n = int(input())
a = [int(x) for x in input().split()]
print(solve(a))
