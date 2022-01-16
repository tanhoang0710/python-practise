# chen dau phay vao de lay ra mang gom cac chu va cac so
# sau do xoa bo cac chu con so
# xoa bo so 0 o dau cac so ma co 0 o dau, neu so la 0000 thi format thanh 0
# sort r in ra kqua
# input la nhieu chuoi nen moi lan lam nhu tren chi dua vao 1 mang nen n chuoi se thanh 1 mang 2 chieu
# can flat thanh mang 1d
def kTra(s):
    a = [str(x) for x in s]
    for ele in a:
        if ele != "0":
            return False
    return True

def fm(s):
    i = 0
    if kTra(s):
        s = "0"
        return s
    while s[i] == "0":
        i += 1
    s = s[i:]
    return s


def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list


def solve1(s):
    for i in range(len(s) - 1, 0, -1):
        if (s[i].isalpha() and s[i - 1].isdigit()) or (s[i].isdigit() and s[i - 1].isalpha()):
            s = s[:i] + "," + s[i:]
    arr = s.split(',')
    res = []
    for ele in arr:
        if ele.isalpha():
            arr.remove(ele)
    for i in range(len(arr)):
        arr[i] = fm(arr[i])
        res.append(int(arr[i]))
    return res


def solve(inp):
    res = []
    for s in inp:
        res.append(solve1(s))
    res = flatten(res)
    res = sorted(res)
    for ele in res:
        print(ele)


t = int(input())
inp = []
while t > 0:
    t -= 1
    s = str(input())
    inp.append(s)
solve(inp)
# s = input()
# kTra(s)


