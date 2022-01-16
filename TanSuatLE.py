t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = [0]*100_005
    for i in range(0, len(arr)):
        count[arr[i]] += 1
    for i in range(len(count)):
        if count[i] != 0:
            if count[i] % 2 == 1:
                print(i)
    # print(count)





# i = 0 count[a[0]] = count[1]++ = 1
# i = 1 count[a[1]] = count[1]++ = 2
# i = 2 count[a[2]] = count[3]++ = 1
# i = 3 count[a[3]] = count[3]++ = 2
# i = 4 count[a[4]] = count[2]++ = 1