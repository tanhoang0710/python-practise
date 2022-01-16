quantity = [int(x) for x in input().split()]
n = quantity[0]
m = quantity[1]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

setArr1 = set(arr1)
setArr2 = set(arr2)

interSection = setArr1.intersection(setArr2)
listIntersection = list(interSection)
sortedListIntersection = sorted(listIntersection)
for ele in sortedListIntersection:
    print(ele, end=' ')
print()

listRes1 = list(setArr1)
res1 = []
for ele in listRes1:
    if arr2.count(ele) == 0:
        res1.append(ele)
sortedRes1 = sorted(res1)
for ele in sortedRes1:
    print(ele, end=' ')
print()

listRes2 = list(setArr2)
res2 = []
for ele in listRes2:
    if arr1.count(ele) == 0:
        res2.append(ele)
sortedRes2 = sorted(res2)
for ele in sortedRes2:
    print(ele, end=' ')
print()