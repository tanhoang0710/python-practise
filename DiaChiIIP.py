def check1(n):
    if n >= 0 and n <= 255:
        return True
    return False


def solve(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for ele in a:
        if not check1(int(ele)):
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if solve(s):
        print('YES')
    else:
        print('NO')