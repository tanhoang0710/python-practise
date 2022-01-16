def solve(a):
    res = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if a[i] > a[j] and i < j:
                res += 1
    print(res)


n = int(input())
a = [int(x) for x in input().split()]
solve(a)
