def check1(s):
    return len(s) >= 3

#5678961
def check(n, s):
    c1, c2 = True, True
    index = -1
    for i in range(0, n + 1):
        if int(s[i]) <= int(s[i - 1]):
            c1 = False
            break
    for i in range(n, len(s) - 1):
        if int(s[i]) >= int(s[i + 1]):
            c2 = False
            break
    return c1 and c2


def solve(s):
    if not check1(s):
        return -1
    for i in range(1, len(s) - 1):
        if check(i, s):
            return i
    return -1


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if solve(s) != -1:
        print('YES')
    else:
        print('NO')