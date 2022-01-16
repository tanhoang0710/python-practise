# def solve(a, k, n):
#     res = []
#     for i in range(0, n + 1):
#         if (a + i) % k == 0 and a + i <= n:
#             res.append(i)
#     if len(res) == 0:
#         print(-1)
#     else:
#         for ele in res:
#             print(ele, end=' ')
#
#
# [a, k, n] = [int(x) for x in input().split()]
# solve(a, k, n)

[a, k, n] = [int(x) for x in input().split()]
res = []
x = 1
while k * x - a <= n - a:
    if k * x - a > 0:
        res.append(k * x - a)
    x += 1

if len(res) > 0:
    for x in res:
        print(x, end=' ')
else:
    print(-1)
