def solve(s):
    tmp = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(tmp[i]) - ord(tmp[i - 1])):
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