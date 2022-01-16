def sumDigit(n):
    sum = 0
    for ele in n:
        sum += int(ele)
    return sum

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    array = [str(x) for x in input().split()]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sumDigit(array[i]) > sumDigit(array[j]):
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
            elif sumDigit(array[i]) == sumDigit(array[j]):
                if int(array[i]) > int(array[j]):
                    tmp2 = array[i]
                    array[i] = array[j]
                    array[j] = tmp2
    # array = sorted(array, key=sumDigit)
    for ele in array:
        print(ele, end=' ')
    print()
