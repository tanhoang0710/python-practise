import re
from operator import itemgetter, attrgetter

def check(s):
    if s == '' or s == ' ':
        return True
    return False


no_of_lines = int(input())
lines = ""
for i in range(no_of_lines):
    lines += input() + ' '
a = re.split('[\s,.?!:;()-/]', lines.lower())
wordArr = []
for ele in a:
    if not check(ele):
        wordArr.append(ele)
tmp = []
for ele in wordArr:
    if ele not in tmp:
        tmp.append(ele)
res = []
for ele in tmp:
    res.append([ele, wordArr.count(ele)])
res = sorted(sorted(res, key=lambda x: x[0], reverse=False), key=lambda x: x[1], reverse=True)
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end=' ')
    print()

# hom 1            la 2
# nay 1            anh 1
# troi 1           dep 1
# dep 1
# mong 1
# la 2
# ko 1
# sao 1
# moi 1
# viec 1
# anh 1
# quan 1
# se 1
# thuan 1
# loi 1