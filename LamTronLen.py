def solve(n):
    # res = ""
    # l = len(s) - 1
    # if int(s[l]) >= 5:
    #     res += '0'
    # else: res += '0'
    # for i in range(l - 1, 1, -1):
    #     if int(s[i + 1] >= 5):
    #         s[i] = s[i] + 1
    #         res += "0"
    #         int(s[i - 1])
    #--------------------------------------
    # a = list(s)
    # l = len(a) - 1
    # for i in range(l + 1):
    #     a[i] = int(a[i])
    # res = '0'
    # for i in range(l - 1, 0, -1):
    #     if a[i + 1] >= 5:
    #         a[i] += 1
    # print(a)
    #---------------------------------------
    x = len(n)
    if int(n) < 10:
        print(n)
    else:
        s = ""
        c = 0
        for i in range(x - 1, 0, -1):
            s = "0" + s
            if int(n[i]) + c < 5:
                c = 0
            else:
                c = 1
        a = str(int(n[0]) + c)
        print(a + s)


t = int(input())

while t > 0:
    s = input()
    solve(s)
    t -= 1
