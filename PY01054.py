def solve(n):
    s = str(n)
    tich = 1
    for i in range(len(s)): # chu y de tich = 1 va bo qua cac chu so '0'
        if s[i] != '0':
            tich *= int(s[i])
    return tich


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    print(solve(n))