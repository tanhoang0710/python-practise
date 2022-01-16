def solve(n):
    sum = 0
    if n % 2 != 0:
        for i in range(1, n + 1, 2):
            sum += 1 / i
    else:
        for i in range(2, n + 1, 2):
            sum += 1 / i
    print("{:.6f}".format(sum))


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    solve(n)