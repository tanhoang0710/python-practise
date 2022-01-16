a = int(input())
b = int(input())
res = str(a - b)
i = 0
# python co co che so nguyen lon
if res == "0":
    print(0)
else:
    while res[i] == "0":
        i += 1
    print(res[i:])