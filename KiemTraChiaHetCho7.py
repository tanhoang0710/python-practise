def solve(n):
    time = 0
    sum = 0
    tmp = n
    while True:
        if n % 7 == 0:
            print(n)
            break
        sum = tmp + int(str(tmp)[::-1])
        tmp = sum
        time += 1
        if sum % 7 == 0:
            print(sum)
            break
        if time > 1000:
            print(-1)
            break


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    solve(n)