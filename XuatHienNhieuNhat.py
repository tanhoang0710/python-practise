# n = int(input())
# count = [0]*100005
# a = [0]*n
# for i in range(n):
#     ele = int(input())
#     a[i] = ele
#     count[a[i]] += 1
#
# res = 0
#
# for i in range(len(count)-1):
#     if count[i] != 0:
#         min_index = i
#         for j in range(i+1, len(count)-1):
#             if count[j] < count[min_index]:
#                 min_index = j
#         count[i], count[min_index] = count[min_index], count[i]
#
# for i in range(len(count)):
#     if count[i] != 0:
#         print(count[i])

def take_second(elem):
    return elem[1]


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    a = [int(x) for x in input().split()]
    countOccur = [0]*100_005
    res = []
    for i in range(0, len(a)):
        countOccur[a[i]] += 1
        res.append([a[i], countOccur[a[i]]])
    res = sorted(res, key=take_second)  #sorted by res[][i]
    if res[-1][1] > int(n / 2):
        print(res[-1][0])
    else:
        print('NO')
    # print(res)




