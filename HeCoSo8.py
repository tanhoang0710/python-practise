s = input()
for i in range(len(s) - 3, 0, -3):
    s = s[:i] + "," + s[i:]
arrSplit = s.split(',')
res = ''
for i in range(len(arrSplit)):
    arrSplit[i] = int(arrSplit[i], 2) # chuyen tu he 2 sang 10
    res += str(arrSplit[i])
print(res)