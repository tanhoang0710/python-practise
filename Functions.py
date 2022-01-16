import re


def check(s):
    arr = ['#', '@', '$']
    t1, t2 = True, False
    if len(s) < 6 or len(s) > 12:
        t1 = False
    for i in range(len(s)):
        if s[i] in arr:
            t2 = True
    pattern = '[a-zA-Z0-9]'
    if re.match(pattern, s) and t1 and t2:
        return True
    return False


t = int(input())
a = []
while t > 0:
    t -= 1
    s = input()
    a.extend(s.split(','))
for ele in a:
    if check(ele):
        print(ele)