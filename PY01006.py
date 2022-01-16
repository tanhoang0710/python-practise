def solve(s):
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7':
            return False
    return True


t = int(input())
while t > 0:
    t -= 1
    s = input()
    if solve(s):
        print("YES")
    else:
        print('NO')