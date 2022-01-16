def solve(s):
    for i in range(len(s) - 1, 0, -1):
        s = s[:i] + "," + s[i:]
    digits = s.split(',')
    sumDigits = 0
    for digit in digits:
        sumDigits += int(digit)

    if sumDigits % 3 == 0:
        print('YES')
    else:
        print('NO')
    # print(str(sumDigits))
    # print(str(sumDigits)[::-1])


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)