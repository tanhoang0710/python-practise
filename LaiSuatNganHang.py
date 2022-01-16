


t = int(input())
while t > 0:
    t -= 1
    inp = [float(x) for x in input().split()]

    n = inp[0]
    x = inp[1]
    m = inp[2]
    sum = n
    res = 0
    while sum < m:
        res += 1
        sum += sum * (x / 100)
    print(res)