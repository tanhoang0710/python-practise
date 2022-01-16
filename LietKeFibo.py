# def solve(a, b):
#     f = [0, 1, 1]
#     for i in range(3, 93):
#         f.append(f[i - 1] + f[i - 2])
#
#     return f
#

t = int(input())
while t > 0:
    t -= 1
    inp = [int(x) for x in input().split()]
    a = inp[0]
    b = inp[1]
    f = [0, 1, 1]
    for i in range(3, 93):
        f.append(f[i - 1] + f[i - 2])

    for i in range(a, b + 1):
        print(f[i], end=' ')
    print()
