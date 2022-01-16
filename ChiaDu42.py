def flatten(input):
    new_list = []
    for i in input:
        for j in i:
            new_list.append(j)
    return new_list


#cach nhap test nhieu dong
test = 10
inp = []
while test > 0:
    data = input()
    base = data.split()
    test -= len(base)
    inp.append(base)
inp = flatten(inp)
res = []
for ele in inp:
    tmp = int(ele) % 42
    res.append(tmp)
res = list(dict.fromkeys(res))
print(len(res))
