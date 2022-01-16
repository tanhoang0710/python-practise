def check(s):
    for i in range(0, len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')
12345678888888888888889
