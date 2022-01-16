def solve(s):
    if len(s) == 1:
        print(1)
        return
    res = 0
    while len(s) != 1:
        sumDigit = 0
        for i in range(1, len(s)):
            sumDigit += int(s[i])
        if s[0] == '-':
            sumDigit += ord('-') - ord('0')
        s = str(sumDigit)
        res += 1
    print(res)


s = input()
solve(s)