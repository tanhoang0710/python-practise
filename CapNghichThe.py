n = int(input())

a = list(map(int, input().split()))
res = 0

for i in range(0, n):
    for j in range(0, n):
        if i < j and a[i] > a[j]:
            res += 1

print(res)
