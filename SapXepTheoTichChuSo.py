def mulDigit(n):
    mul = 1
    for ele in n:
        if ele != 0:
            mul *= int(ele)
    return mul

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    array = [str(x) for x in input().split()]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if mulDigit(array[i]) > mulDigit(array[j]):
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
            elif mulDigit(array[i]) == mulDigit(array[j]):
                if int(array[i]) > int(array[j]):
                    tmp2 = array[i]
                    array[i] = array[j]
                    array[j] = tmp2
    for ele in array:
        print(ele, end=' ')
    print()
