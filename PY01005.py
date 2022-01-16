def solve(s):
    countF = 0
    countS = 0
    for i in range(len(s)):
        if s[i] == '4':
            countF += 1
        if s[i] == '7':
            countS += 1
    if countS + countF == 4 or countS + countF == 7:
        return True
    return False


s = input()
if solve(s):
    print('YES')
else:
    print('NO')