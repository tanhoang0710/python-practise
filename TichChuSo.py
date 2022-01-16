def solve(s):
    for i in range(len(s) - 1, 0, -1):
        s = s[:i] + "," + s[i:]
    digits = s.split(',')
    res = 1
    for digit in digits:
        if digit != "0":
            res *= int(digit)
    print(res)
    # print(str(sumDigits))
    # print(str(sumDigits)[::-1])


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)