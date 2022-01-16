
def solve(str):
    s = []
    for z in range(len(str)):
        s.append(str[z])
    i = len(s) - 1
    while s[i] >= s[i - 1] and i > 0:
        i -= 1
    if i <= 0:
        print('-1')
    else:
        j = len(s) - 1
        while s[j] >= s[i - 1]:
            j -= 1
        k = j
        while s[k - 1] == s[k]:
            k -= 1
        s[k], s[i - 1] = s[i - 1], s[k]
        if s[0] == '0':
            print(-1)
        else:
            for ele in s:
                print(ele, end='')
            print()


t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1
