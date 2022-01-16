p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp = [str(x) for x in input().split()]
    k = int(inp[0])

    if k == 0:
        break
    else: s = inp[1]
    res = ""
    for i in range(len(s)):
        index = p.index(s[i])
        res += p[(index + k) % 28]
    print(res[::-1]) # reverse String