def solve(s):
    for i in range(len(s) - 1, 0, -1):
        s = s[:i] + "," + s[i:]
    digits = s.split(',')
    check1 = True
    check2 = True
    check3 = True
    if len(digits) % 2 == 0: check1 = False
    if int(digits[0]) == int(digits[1]): check2 = False
    for i in range(0, len(digits) - 2, 2):
        if int(digits[i]) != int(digits[i + 2]): check3 = False

    if check1 and check2 and check3:
        print('YES')
    else:
        print('NO')


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)