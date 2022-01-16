def solve(a):
    a = sorted(a)
    for i in range(1, len(a)):
        if a[i] - a[i - 1] != 1:
            return a[i - 1] + 1
    return a[len(a) - 1] + 1


n = int(input())
a = [int(x) for x in input().split()]
print(solve(a))