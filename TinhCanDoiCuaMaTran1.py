n = int(input())
arr = []
for i in range(n):
    tmp = [int(x) for x in input().split()]
    arr.append(tmp)
k = int(input())
# 2  8 10  6  7
#
# 6  3  2  6  9
#
# 10 2  6  2  8
#
# 9  9  7  9  8
#
# 9  6  5  6  9
# Tinh tong phan tu tam giac tren tru tong phan tu tam giac duoi roi so sanh vs k
top, bottom = 0, 0
for i in range(0, n):
    for j in range(i + 1, n):
        top += arr[i][j]
    for j in range(0, i):
        bottom += arr[i][j]
hieu = abs(top - bottom)
res = 'YES' if hieu <= k else 'NO'
print(res)
print(hieu)
