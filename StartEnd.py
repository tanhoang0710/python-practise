
def check(s):
    if s[-2:] == s[0:2]:
        print('YES')
    else:
        print('NO')


t = int(input())
while t > 0:
    t -= 1
    s = input()
    check(s)
