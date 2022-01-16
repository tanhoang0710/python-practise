def solve(s):
    # countArr = []
    # tmp = s
    # tmp = list(dict.fromkeys(tmp));
    # for i in range(0, len(tmp)):
    #     countArr.append(s.count(tmp[i]))
    #
    # res = []
    # for i in range(0, len(tmp)):
    #     ele = str(countArr[i]) + tmp[i]
    #     res.append(ele)
    # for ele in res:
    #     print(ele, end='')
    # print()
    # print(countArr)
    # print(tmp)
    count = 1
    l = len(s)
    for i in range(0, l - 1, 1):
        if s[i] == s[i + 1]: count += 1
        else:
            print(count, s[i], sep='', end='')
            count = 1
    print(count, s[l - 1], sep='', end='')
    print()


t = int(input())
while t > 0:
    t -= 1
    s = input()
    solve(s)
