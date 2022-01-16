def check(s):
    for i in range(0, len(s), 2):
        if s[i] >= "1" and s[i] <= "9":
            return False
    return True


def solve(s):
    sum = 0
    mul = 1
    for i in range(len(s)):
        if i % 2 != 0:
            sum += int(s[i])
        else:
            if s[i] != "0":
                mul *= int(s[i])
    if check(s):
        mul = 0
    print(mul, sum)


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)