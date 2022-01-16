def check1(s):
    return len(set(list(s))) == 2


def check2(s):
    s1 = ''
    s2 = ''
    for i in range(len(s)):
        if i % 2 == 0:
            s1 += s[i]
        else:
            s2 += s[i]
    return len(set(list(s1))) == 1 and len(set(list(s2))) == 1


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check1(s) and check2(s):
        print('YES')
    else:
        print('NO')