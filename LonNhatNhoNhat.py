

while True:
    n = int(input())
    if n == 0:
        break
    min = 1e99
    max = 0
    for i in range(n):
        ele = int(input())
        if ele != min and ele != max:
            if ele > max: max = ele
            if ele < min: min = ele
    if min == max:
        print("BANG NHAU")
    else: print(min, max)
