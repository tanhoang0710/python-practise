def check1(n):
    s = str(n)
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return False
    return True


def check2(n):
    s = str(n)
    t = 0
    for i in range(len(s)):
        t += int(s[i])
    return t % 10 == 0


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if check1(n) and check2(n):
        print('YES')
    else:
        print('NO')