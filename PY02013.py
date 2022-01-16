def solve(n):
    if n == 1:
        print(1)
        return
    res = []
    while n != 1:
        if n % 2 == 0:
            n = int(n/2)
            res.append(n)
        else:
            n = n * 3 + 1
            res.append(n)
    print(len(res) + 1)


while True:
    n = int(input())
    if n == 0:
        break
    solve(n)
