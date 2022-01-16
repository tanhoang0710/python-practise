def solve(a):
    for i in range(n - 1):
        if a[i + 1] - a[i] != 1:
            return a[i] + 1
    return a[len(a) - 1] + 1


n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)

print(solve(a))
