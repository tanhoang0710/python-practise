def check1(n):
    return len(str(n)) % 2 == 1


def check2(n):
    s = str(n)
    return s[0] != s[1]


def check3(n):
    s = str(n)
    for i in range(0, len(s) - 1, 2):
        if s[i] != s[i + 2]:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    if check1(n) and check2(n) and check3(n):
        print("YES")
    else:
        print('NO')