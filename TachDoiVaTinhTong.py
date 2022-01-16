def solve(s):
    while len(s) > 1:
        s1 = s[:(len(s)//2)]
        s2 = s[len(s)//2:]
        sum = int(s1) + int(s2)
        print(sum)
        s = str(sum)


s = input()
solve(s)
