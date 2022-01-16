def check1(s):
    # kiem tra xau chi vo 6 va 8 hay ko
    for i in range(len(s)):
        if s[i] != '6' and s[i] != '8':
            return False
    return True


def check2(s):
    if s[0] == '8':
        return False
    for i in range(len(s)):
        if s[i] == '8' and s[i - 1] != '6' and s[i - 1] != '8':
            return False
        if i > 1 and s[i] == '8' and s[i - 1] == '8' and s[i - 2] != '6':
            return False
    return True


def solve(s):
    if check1(s) and check2(s):
        return True
    return False


s = input()
if solve(s):
    print('YES')
else:
    print('NO')
