def check(s):
    a = ['0', '1', '2']
    for i in range(len(s)):
        if s[i] not in a:
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s):
        print("YES")
    else:
        print('NO')