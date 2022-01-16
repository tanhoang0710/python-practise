quantity = [int(x) for x in input().split()]
n = quantity[0]
m = quantity[1]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

setArr1 = set(arr1)
setArr2 = set(arr2)

interSection = setArr1.intersection(setArr2)
if interSection == setArr1:
    print('YES')
else:
    print('NO')