rows, cols = (11, 11)
arr = [[0 for i in range(cols)] for j in range(rows)]
for i in range(0, 11):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j] + arr[i - 1][j - 1]


def solve(n, p, x):
    res = arr[x][n] * p**n * (1 - p)**(x - n)
    print(res)


t = int(input())
while t > 0:
    t -= 1
    s = input()
    aa = [str(x) for x in s.split()]
    n = int(aa[0])
    p = float(aa[1])
    x = int(aa[2])
    solve(n, p, x)
